import requests
import json
from websocket import create_connection

recordRoute = "/record/"
recordQueryRoute = "/record/query/"

statusOk = 200
statusCreated = 201

# --- DB {{{
class DB:
    """
    host     string
    username string
    password string
    """

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def _endpoint(self, route):
        """ Constructs a fully qualified endpoint using the host """
        return "http://" + self.host + route

    def _query(self, kind, attrs, skip, limit):
        """
            The heart of the databasae querying, builds up the context
            for querying a record time and translates that query into
            a list of []RecordData


            Remember a user of the database calls recordData.transfer(record)
        """
        r = requests.post(self._endpoint(recordQueryRoute), auth=(self.username, self.password), params={
            "kind": kind,
            "skip": skip,
            "limit": limit
        }, data=attrs)

        if r.status_code != statusOk:
            raise Exception("db._query Bad response from server", r.text)
            return

        records = []
        for json in r.json():
            records.append(RecordData(kind, json))
        return records

    # --- save(record) {{{
    def save(self, record):
        r = requests.post(self._endpoint(recordRoute), auth=(self.username, self.password), params={
            "kind": record.kind(),
            "id": record.id,
        }, data=record.marshal())

        if r.status_code == statusOk or r.status_code == statusCreated:
            record.unmarshal(r.json())
        else:
            raise Exception("db.save Bad response from server", r.text)
     # --- }}}

    # --- delete(record) {{{
    def delete(self, record):
        r = requests.delete(self._endpoint(recordRoute), auth=(self.username, self.password), params={
            "kind": record.kind(),
            "id": record.id,
        })

        if r.status_code == statusOk:
            return
        else:
            raise Exception("db.delete Bad response from server", r.text)
    # --- }}}

    # --- get(id, recordClass) {{{{
    def get(self, recordClass, id):
        """
            classic gaia GET /record/?kind=<kind>&id=<id>
        """
        r = requests.get(self._endpoint(recordRoute), auth=(self.username, self.password), params={
            "kind": recordClass.Kind(),
            "id": id,
        })

        if r.status_code == statusOk:
            return recordClass.unmarshal(r.json())
        else:
            eString = "db.get(%s, %s) Bad response from server" % (recordClass.Kind(), id)
            raise Exception(eString, r.text)

    # --- }}}

    # --- query(kind) {{{
    def query(self, kind):
        """
            Constructs a Query object, which is purely a builder object
        """
        return Query(kind, self)
    # --- }}}

    # --- changes() {{{
    def changes(self):
        """
            Changes opens a socket to gaia, and then returns the
            changes of class Change.
        """
        ws = create_connection("ws://%s/record/changes/?public=%s&private=%s" % (self.host, self.username, self.password))
        for result in ws:
            yield Change.unmarshal(json.loads(result))
    # --- }}}

# --- DB }}}

# --- Query {{{
class Query:
    """
    db       DB
    kind     string
    limit    int
    skip     int
    attrs    map[string]any
    """

    def __init__(self, kind, db):
        self._skip = 0
        self._limit = 0
        self._attrs = {}

        self.kind = kind
        self.db = db

    def limit(self, i):
        self._limit = i
        return self

    def skip(self, i):
        self._skip = i
        return self

    def select(self, attrs):
        self._attrs = attrs
        return self

    def execute(self):
        return self.db._query(self.kind, self._attrs, self._skip, self._limit)

# --- }}}

# --- Change {{{
Update = 1
Delete = 2


class Change:
    """
    change_kind
    record_kind
    record_data
    """

    def __init__(self, changekind, recordkind, recorddata):
        self.change_kind = changekind
        self.record_kind = recordkind
        self.record_data = recorddata

    @staticmethod
    def unmarshal(json):
        return Change(json["change_kind"], json["record_kind"], RecordData(json["record_kind"], json["record"]))
# --- }}}

# --- RecordData {{{
class RecordData:
    """
    kind    string
    json    map[string]any
    """

    def __init__(self, kind, json):
        self.kind = kind
        self.json = json

    def unmarshal(self, recordClass):
        if self.kind != recordClass.Kind():
            raise Exception("Kinds don't match")

        return recordClass.unmarshal(self.json)
# --- }}}

# --- Record {{{
class Record:
    def __init__(self, id=None):
        if id is None:
            return

        self.id = id
# --- }}}
