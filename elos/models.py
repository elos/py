
    

import dateutil.parser
from elos.db import Record


ActionKind = "action" 
AttributeKind = "attribute" 
CalendarKind = "calendar" 
ContextKind = "context" 
CredentialKind = "credential" 
DatumKind = "datum" 
EventKind = "event" 
FixtureKind = "fixture" 
GroupKind = "group" 
HabitKind = "habit" 
LinkKind = "link" 
LocationKind = "location" 
MediaKind = "media" 
ModelKind = "model" 
NoteKind = "note" 
ObjectKind = "object" 
OntologyKind = "ontology" 
PersonKind = "person" 
ProfileKind = "profile" 
QuantityKind = "quantity" 
RelationKind = "relation" 
RoutineKind = "routine" 
ScheduleKind = "schedule" 
SessionKind = "session" 
TagKind = "tag" 
TaskKind = "task" 
TraitKind = "trait" 
UserKind = "user" 


class Action(Record):
    """ 
    completed bool 
    created_at DateTime 
    end_time DateTime 
    id str 
    name str 
    start_time DateTime 
    updated_at DateTime  
    actionable []str 
    owner []str 
    person []str 
    task []str 
    """

    
     
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      
    
    def person(self, db): 
        if self.person_id != None:
            return db.get(Person, self.person_id)
        else:
            return None
      
    
    def task(self, db): 
        if self.task_id != None:
            return db.get(Task, self.task_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["completed"] = self.completed 
        json["created_at"] = self.created_at.isoformat() 
        json["end_time"] = self.end_time.isoformat() 
        json["id"] = self.id 
        json["name"] = self.name 
        json["start_time"] = self.start_time.isoformat() 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["actionable_id"] = self.actionable_id 
        json["owner_id"] = self.owner_id 
        json["person_id"] = self.person_id 
        json["task_id"] = self.task_id 

        return json


    @staticmethod
    def Kind():
        return ActionKind

    @staticmethod
    def unmarshal(json):
        self = Action()

        # Traits 
        self.completed = json["completed"] 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.end_time = dateutil.parser.parse(json["end_time"]) 
        self.id = json["id"] 
        self.name = json["name"] 
        self.start_time = dateutil.parser.parse(json["start_time"]) 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.actionable_id = json["actionable_id"] 
        self.owner_id = json["owner_id"] 
        self.person_id = json["person_id"] 
        self.task_id = json["task_id"] 

        return self

class Attribute(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    updated_at DateTime 
    value str  
    object []str 
    owner []str 
    trait []str 
    """

    
    
    def object(self, db): 
        if self.object_id != None:
            return db.get(Object, self.object_id)
        else:
            return None
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      
    
    def trait(self, db): 
        if self.trait_id != None:
            return db.get(Trait, self.trait_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["updated_at"] = self.updated_at.isoformat() 
        json["value"] = self.value 

        # Relations 
        json["object_id"] = self.object_id 
        json["owner_id"] = self.owner_id 
        json["trait_id"] = self.trait_id 

        return json


    @staticmethod
    def Kind():
        return AttributeKind

    @staticmethod
    def unmarshal(json):
        self = Attribute()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 
        self.value = json["value"] 

        # Relations 
        self.object_id = json["object_id"] 
        self.owner_id = json["owner_id"] 
        self.trait_id = json["trait_id"] 

        return self

class Calendar(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    name str 
    updated_at DateTime 
    weekday_schedules map[str]str 
    yearday_schedules map[str]str  
    base_schedule []str 
    fixtures str 
    manifest_fixture []str 
    owner []str 
    """

    
    
    def base_schedule(self, db): 
        if self.base_schedule_id != None:
            return db.get(Schedule, self.base_schedule_id)
        else:
            return None
      
    
    def fixtures(self, db): 
        [db.get(Fixture, id) for id in self.fixtures_ids]
      
    
    def manifest_fixture(self, db): 
        if self.manifest_fixture_id != None:
            return db.get(Fixture, self.manifest_fixture_id)
        else:
            return None
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["name"] = self.name 
        json["updated_at"] = self.updated_at.isoformat() 
        json["weekday_schedules"] = self.weekday_schedules 
        json["yearday_schedules"] = self.yearday_schedules 

        # Relations 
        json["base_schedule_id"] = self.base_schedule_id 
        json["fixtures_ids"] = self.fixtures_ids 
        json["manifest_fixture_id"] = self.manifest_fixture_id 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return CalendarKind

    @staticmethod
    def unmarshal(json):
        self = Calendar()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.name = json["name"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 
        self.weekday_schedules = json["weekday_schedules"] 
        self.yearday_schedules = json["yearday_schedules"] 

        # Relations 
        self.base_schedule_id = json["base_schedule_id"] 
        self.fixtures_ids = json["fixtures_ids"] 
        self.manifest_fixture_id = json["manifest_fixture_id"] 
        self.owner_id = json["owner_id"] 

        return self

class Context(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    domain str 
    id str 
    ids []str 
    updated_at DateTime  
    owner []str 
    """

    
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["domain"] = self.domain 
        json["id"] = self.id 
        json["ids"] = self.ids 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return ContextKind

    @staticmethod
    def unmarshal(json):
        self = Context()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.domain = json["domain"] 
        self.id = json["id"] 
        self.ids = json["ids"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.owner_id = json["owner_id"] 

        return self

class Credential(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    name str 
    private str 
    public str 
    spec str 
    updated_at DateTime  
    owner []str 
    sessions str 
    """

    
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      
    
    def sessions(self, db): 
        [db.get(Session, id) for id in self.sessions_ids]
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["name"] = self.name 
        json["private"] = self.private 
        json["public"] = self.public 
        json["spec"] = self.spec 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["owner_id"] = self.owner_id 
        json["sessions_ids"] = self.sessions_ids 

        return json


    @staticmethod
    def Kind():
        return CredentialKind

    @staticmethod
    def unmarshal(json):
        self = Credential()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.name = json["name"] 
        self.private = json["private"] 
        self.public = json["public"] 
        self.spec = json["spec"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.owner_id = json["owner_id"] 
        self.sessions_ids = json["sessions_ids"] 

        return self

class Datum(Record):
    """ 
    context str 
    created_at DateTime 
    id str 
    tags []str 
    unit str 
    value float  
    event []str 
    owner []str 
    person []str 
    """

    
    
    def event(self, db): 
        if self.event_id != None:
            return db.get(Event, self.event_id)
        else:
            return None
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      
    
    def person(self, db): 
        if self.person_id != None:
            return db.get(Person, self.person_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["context"] = self.context 
        json["created_at"] = self.created_at.isoformat() 
        json["id"] = self.id 
        json["tags"] = self.tags 
        json["unit"] = self.unit 
        json["value"] = self.value 

        # Relations 
        json["event_id"] = self.event_id 
        json["owner_id"] = self.owner_id 
        json["person_id"] = self.person_id 

        return json


    @staticmethod
    def Kind():
        return DatumKind

    @staticmethod
    def unmarshal(json):
        self = Datum()

        # Traits 
        self.context = json["context"] 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.id = json["id"] 
        self.tags = json["tags"] 
        self.unit = json["unit"] 
        self.value = json["value"] 

        # Relations 
        self.event_id = json["event_id"] 
        self.owner_id = json["owner_id"] 
        self.person_id = json["person_id"] 

        return self

class Event(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    name str 
    time DateTime 
    updated_at DateTime  
    location []str 
    media []str 
    note []str 
    owner []str 
    prior []str 
    quantity []str 
    tags str 
    """

    
    
    def location(self, db): 
        if self.location_id != None:
            return db.get(Location, self.location_id)
        else:
            return None
      
    
    def media(self, db): 
        if self.media_id != None:
            return db.get(Media, self.media_id)
        else:
            return None
      
    
    def note(self, db): 
        if self.note_id != None:
            return db.get(Note, self.note_id)
        else:
            return None
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      
    
    def prior(self, db): 
        if self.prior_id != None:
            return db.get(Event, self.prior_id)
        else:
            return None
      
    
    def quantity(self, db): 
        if self.quantity_id != None:
            return db.get(Quantity, self.quantity_id)
        else:
            return None
      
    
    def tags(self, db): 
        [db.get(Tag, id) for id in self.tags_ids]
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["name"] = self.name 
        json["time"] = self.time.isoformat() 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["location_id"] = self.location_id 
        json["media_id"] = self.media_id 
        json["note_id"] = self.note_id 
        json["owner_id"] = self.owner_id 
        json["prior_id"] = self.prior_id 
        json["quantity_id"] = self.quantity_id 
        json["tags_ids"] = self.tags_ids 

        return json


    @staticmethod
    def Kind():
        return EventKind

    @staticmethod
    def unmarshal(json):
        self = Event()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.name = json["name"] 
        self.time = dateutil.parser.parse(json["time"]) 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.location_id = json["location_id"] 
        self.media_id = json["media_id"] 
        self.note_id = json["note_id"] 
        self.owner_id = json["owner_id"] 
        self.prior_id = json["prior_id"] 
        self.quantity_id = json["quantity_id"] 
        self.tags_ids = json["tags_ids"] 

        return self

class Fixture(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    end_time DateTime 
    exceptions []Datetime 
    expires_at DateTime 
    id str 
    label bool 
    name str 
    rank int 
    start_time DateTime 
    updated_at DateTime  
    actionable []str 
    actions str 
    eventable []str 
    events str 
    owner []str 
    """

    
     
    
    def actions(self, db): 
        [db.get(Action, id) for id in self.actions_ids]
      
     
    
    def events(self, db): 
        [db.get(Event, id) for id in self.events_ids]
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["end_time"] = self.end_time.isoformat() 
        json["exceptions"] = [d.isoformat() for d in self.exceptions] 
        json["expires_at"] = self.expires_at.isoformat() 
        json["id"] = self.id 
        json["label"] = self.label 
        json["name"] = self.name 
        json["rank"] = self.rank 
        json["start_time"] = self.start_time.isoformat() 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["actionable_id"] = self.actionable_id 
        json["actions_ids"] = self.actions_ids 
        json["eventable_id"] = self.eventable_id 
        json["events_ids"] = self.events_ids 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return FixtureKind

    @staticmethod
    def unmarshal(json):
        self = Fixture()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.end_time = dateutil.parser.parse(json["end_time"]) 
        self.exceptions = map(dateutil.parser.parse, json["exceptions"]) 
        self.expires_at = dateutil.parser.parse(json["expires_at"]) 
        self.id = json["id"] 
        self.label = json["label"] 
        self.name = json["name"] 
        self.rank = json["rank"] 
        self.start_time = dateutil.parser.parse(json["start_time"]) 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.actionable_id = json["actionable_id"] 
        self.actions_ids = json["actions_ids"] 
        self.eventable_id = json["eventable_id"] 
        self.events_ids = json["events_ids"] 
        self.owner_id = json["owner_id"] 

        return self

class Group(Record):
    """ 
    access int 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    name str 
    updated_at DateTime  
    contexts str 
    grantees str 
    owner []str 
    """

    
    
    def contexts(self, db): 
        [db.get(Context, id) for id in self.contexts_ids]
      
    
    def grantees(self, db): 
        [db.get(User, id) for id in self.grantees_ids]
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["access"] = self.access 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["name"] = self.name 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["contexts_ids"] = self.contexts_ids 
        json["grantees_ids"] = self.grantees_ids 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return GroupKind

    @staticmethod
    def unmarshal(json):
        self = Group()

        # Traits 
        self.access = json["access"] 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.name = json["name"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.contexts_ids = json["contexts_ids"] 
        self.grantees_ids = json["grantees_ids"] 
        self.owner_id = json["owner_id"] 

        return self

class Habit(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    name str 
    updated_at DateTime  
    checkins str 
    owner []str 
    tag []str 
    """

    
    
    def checkins(self, db): 
        [db.get(Event, id) for id in self.checkins_ids]
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      
    
    def tag(self, db): 
        if self.tag_id != None:
            return db.get(Tag, self.tag_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["name"] = self.name 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["checkins_ids"] = self.checkins_ids 
        json["owner_id"] = self.owner_id 
        json["tag_id"] = self.tag_id 

        return json


    @staticmethod
    def Kind():
        return HabitKind

    @staticmethod
    def unmarshal(json):
        self = Habit()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.name = json["name"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.checkins_ids = json["checkins_ids"] 
        self.owner_id = json["owner_id"] 
        self.tag_id = json["tag_id"] 

        return self

class Link(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    ids map[int]str 
    updated_at DateTime  
    object []str 
    owner []str 
    relation []str 
    """

    
    
    def object(self, db): 
        if self.object_id != None:
            return db.get(Object, self.object_id)
        else:
            return None
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      
    
    def relation(self, db): 
        if self.relation_id != None:
            return db.get(Relation, self.relation_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["ids"] = self.ids 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["object_id"] = self.object_id 
        json["owner_id"] = self.owner_id 
        json["relation_id"] = self.relation_id 

        return json


    @staticmethod
    def Kind():
        return LinkKind

    @staticmethod
    def unmarshal(json):
        self = Link()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.ids = json["ids"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.object_id = json["object_id"] 
        self.owner_id = json["owner_id"] 
        self.relation_id = json["relation_id"] 

        return self

class Location(Record):
    """ 
    altitude float 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    latitude float 
    longitude float 
    updated_at DateTime  
    owner []str 
    """

    
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["altitude"] = self.altitude 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["latitude"] = self.latitude 
        json["longitude"] = self.longitude 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return LocationKind

    @staticmethod
    def unmarshal(json):
        self = Location()

        # Traits 
        self.altitude = json["altitude"] 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.latitude = json["latitude"] 
        self.longitude = json["longitude"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.owner_id = json["owner_id"] 

        return self

class Media(Record):
    """ 
    codec str 
    content str 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    updated_at DateTime  
    owner []str 
    """

    
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["codec"] = self.codec 
        json["content"] = self.content 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return MediaKind

    @staticmethod
    def unmarshal(json):
        self = Media()

        # Traits 
        self.codec = json["codec"] 
        self.content = json["content"] 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.owner_id = json["owner_id"] 

        return self

class Model(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    name str 
    updated_at DateTime  
    objects str 
    ontology []str 
    owner []str 
    relations str 
    traits str 
    """

    
    
    def objects(self, db): 
        [db.get(Object, id) for id in self.objects_ids]
      
    
    def ontology(self, db): 
        if self.ontology_id != None:
            return db.get(Ontology, self.ontology_id)
        else:
            return None
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      
    
    def relations(self, db): 
        [db.get(Relation, id) for id in self.relations_ids]
      
    
    def traits(self, db): 
        [db.get(Trait, id) for id in self.traits_ids]
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["name"] = self.name 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["objects_ids"] = self.objects_ids 
        json["ontology_id"] = self.ontology_id 
        json["owner_id"] = self.owner_id 
        json["relations_ids"] = self.relations_ids 
        json["traits_ids"] = self.traits_ids 

        return json


    @staticmethod
    def Kind():
        return ModelKind

    @staticmethod
    def unmarshal(json):
        self = Model()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.name = json["name"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.objects_ids = json["objects_ids"] 
        self.ontology_id = json["ontology_id"] 
        self.owner_id = json["owner_id"] 
        self.relations_ids = json["relations_ids"] 
        self.traits_ids = json["traits_ids"] 

        return self

class Note(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    text str 
    updated_at DateTime  
    owner []str 
    """

    
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["text"] = self.text 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return NoteKind

    @staticmethod
    def unmarshal(json):
        self = Note()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.text = json["text"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.owner_id = json["owner_id"] 

        return self

class Object(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    updated_at DateTime  
    attributes str 
    links str 
    model []str 
    ontology []str 
    owner []str 
    """

    
    
    def attributes(self, db): 
        [db.get(Attribute, id) for id in self.attributes_ids]
      
    
    def links(self, db): 
        [db.get(Link, id) for id in self.links_ids]
      
    
    def model(self, db): 
        if self.model_id != None:
            return db.get(Model, self.model_id)
        else:
            return None
      
    
    def ontology(self, db): 
        if self.ontology_id != None:
            return db.get(Ontology, self.ontology_id)
        else:
            return None
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["attributes_ids"] = self.attributes_ids 
        json["links_ids"] = self.links_ids 
        json["model_id"] = self.model_id 
        json["ontology_id"] = self.ontology_id 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return ObjectKind

    @staticmethod
    def unmarshal(json):
        self = Object()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.attributes_ids = json["attributes_ids"] 
        self.links_ids = json["links_ids"] 
        self.model_id = json["model_id"] 
        self.ontology_id = json["ontology_id"] 
        self.owner_id = json["owner_id"] 

        return self

class Ontology(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    updated_at DateTime  
    models str 
    objects str 
    owner []str 
    """

    
    
    def models(self, db): 
        [db.get(Model, id) for id in self.models_ids]
      
    
    def objects(self, db): 
        [db.get(Object, id) for id in self.objects_ids]
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["models_ids"] = self.models_ids 
        json["objects_ids"] = self.objects_ids 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return OntologyKind

    @staticmethod
    def unmarshal(json):
        self = Ontology()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.models_ids = json["models_ids"] 
        self.objects_ids = json["objects_ids"] 
        self.owner_id = json["owner_id"] 

        return self

class Person(Record):
    """ 
    created_at DateTime 
    first_name str 
    id str 
    last_name str 
    name str 
    updated_at DateTime  
    notes str 
    owner []str 
    """

    
    
    def notes(self, db): 
        [db.get(Note, id) for id in self.notes_ids]
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["first_name"] = self.first_name 
        json["id"] = self.id 
        json["last_name"] = self.last_name 
        json["name"] = self.name 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["notes_ids"] = self.notes_ids 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return PersonKind

    @staticmethod
    def unmarshal(json):
        self = Person()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.first_name = json["first_name"] 
        self.id = json["id"] 
        self.last_name = json["last_name"] 
        self.name = json["name"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.notes_ids = json["notes_ids"] 
        self.owner_id = json["owner_id"] 

        return self

class Profile(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    email str 
    id str 
    name str 
    phone str 
    updated_at DateTime  
    actions str 
    calendar []str 
    current_action []str 
    current_actionable []str 
    data str 
    events str 
    location []str 
    ontology []str 
    owner []str 
    routines str 
    tasks str 
    """

    
    
    def actions(self, db): 
        [db.get(Action, id) for id in self.actions_ids]
      
    
    def calendar(self, db): 
        if self.calendar_id != None:
            return db.get(Calendar, self.calendar_id)
        else:
            return None
      
    
    def current_action(self, db): 
        if self.current_action_id != None:
            return db.get(Action, self.current_action_id)
        else:
            return None
      
     
    
    def data(self, db): 
        [db.get(Datum, id) for id in self.data_ids]
      
    
    def events(self, db): 
        [db.get(Event, id) for id in self.events_ids]
      
    
    def location(self, db): 
        if self.location_id != None:
            return db.get(Location, self.location_id)
        else:
            return None
      
    
    def ontology(self, db): 
        if self.ontology_id != None:
            return db.get(Ontology, self.ontology_id)
        else:
            return None
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      
    
    def routines(self, db): 
        [db.get(Routine, id) for id in self.routines_ids]
      
    
    def tasks(self, db): 
        [db.get(Task, id) for id in self.tasks_ids]
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["email"] = self.email 
        json["id"] = self.id 
        json["name"] = self.name 
        json["phone"] = self.phone 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["actions_ids"] = self.actions_ids 
        json["calendar_id"] = self.calendar_id 
        json["current_action_id"] = self.current_action_id 
        json["current_actionable_id"] = self.current_actionable_id 
        json["data_ids"] = self.data_ids 
        json["events_ids"] = self.events_ids 
        json["location_id"] = self.location_id 
        json["ontology_id"] = self.ontology_id 
        json["owner_id"] = self.owner_id 
        json["routines_ids"] = self.routines_ids 
        json["tasks_ids"] = self.tasks_ids 

        return json


    @staticmethod
    def Kind():
        return ProfileKind

    @staticmethod
    def unmarshal(json):
        self = Profile()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.email = json["email"] 
        self.id = json["id"] 
        self.name = json["name"] 
        self.phone = json["phone"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.actions_ids = json["actions_ids"] 
        self.calendar_id = json["calendar_id"] 
        self.current_action_id = json["current_action_id"] 
        self.current_actionable_id = json["current_actionable_id"] 
        self.data_ids = json["data_ids"] 
        self.events_ids = json["events_ids"] 
        self.location_id = json["location_id"] 
        self.ontology_id = json["ontology_id"] 
        self.owner_id = json["owner_id"] 
        self.routines_ids = json["routines_ids"] 
        self.tasks_ids = json["tasks_ids"] 

        return self

class Quantity(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    unit str 
    updated_at DateTime 
    value float  
    owner []str 
    """

    
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["unit"] = self.unit 
        json["updated_at"] = self.updated_at.isoformat() 
        json["value"] = self.value 

        # Relations 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return QuantityKind

    @staticmethod
    def unmarshal(json):
        self = Quantity()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.unit = json["unit"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 
        self.value = json["value"] 

        # Relations 
        self.owner_id = json["owner_id"] 

        return self

class Relation(Record):
    """ 
    codomain str 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    inverse str 
    multiplicity str 
    name str 
    updated_at DateTime  
    links str 
    model []str 
    owner []str 
    """

    
    
    def links(self, db): 
        [db.get(Link, id) for id in self.links_ids]
      
    
    def model(self, db): 
        if self.model_id != None:
            return db.get(Model, self.model_id)
        else:
            return None
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["codomain"] = self.codomain 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["inverse"] = self.inverse 
        json["multiplicity"] = self.multiplicity 
        json["name"] = self.name 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["links_ids"] = self.links_ids 
        json["model_id"] = self.model_id 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return RelationKind

    @staticmethod
    def unmarshal(json):
        self = Relation()

        # Traits 
        self.codomain = json["codomain"] 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.inverse = json["inverse"] 
        self.multiplicity = json["multiplicity"] 
        self.name = json["name"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.links_ids = json["links_ids"] 
        self.model_id = json["model_id"] 
        self.owner_id = json["owner_id"] 

        return self

class Routine(Record):
    """ 
    created_at DateTime 
    end_time DateTime 
    id str 
    name str 
    start_time DateTime 
    updated_at DateTime  
    actions str 
    completed_tasks str 
    current_action []str 
    owner []str 
    tasks str 
    """

    
    
    def actions(self, db): 
        [db.get(Action, id) for id in self.actions_ids]
      
    
    def completed_tasks(self, db): 
        [db.get(Task, id) for id in self.completed_tasks_ids]
      
    
    def current_action(self, db): 
        if self.current_action_id != None:
            return db.get(Action, self.current_action_id)
        else:
            return None
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      
    
    def tasks(self, db): 
        [db.get(Task, id) for id in self.tasks_ids]
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["end_time"] = self.end_time.isoformat() 
        json["id"] = self.id 
        json["name"] = self.name 
        json["start_time"] = self.start_time.isoformat() 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["actions_ids"] = self.actions_ids 
        json["completed_tasks_ids"] = self.completed_tasks_ids 
        json["current_action_id"] = self.current_action_id 
        json["owner_id"] = self.owner_id 
        json["tasks_ids"] = self.tasks_ids 

        return json


    @staticmethod
    def Kind():
        return RoutineKind

    @staticmethod
    def unmarshal(json):
        self = Routine()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.end_time = dateutil.parser.parse(json["end_time"]) 
        self.id = json["id"] 
        self.name = json["name"] 
        self.start_time = dateutil.parser.parse(json["start_time"]) 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.actions_ids = json["actions_ids"] 
        self.completed_tasks_ids = json["completed_tasks_ids"] 
        self.current_action_id = json["current_action_id"] 
        self.owner_id = json["owner_id"] 
        self.tasks_ids = json["tasks_ids"] 

        return self

class Schedule(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    end_time DateTime 
    id str 
    name str 
    start_time DateTime 
    updated_at DateTime  
    fixtures str 
    owner []str 
    """

    
    
    def fixtures(self, db): 
        [db.get(Fixture, id) for id in self.fixtures_ids]
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["end_time"] = self.end_time.isoformat() 
        json["id"] = self.id 
        json["name"] = self.name 
        json["start_time"] = self.start_time.isoformat() 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["fixtures_ids"] = self.fixtures_ids 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return ScheduleKind

    @staticmethod
    def unmarshal(json):
        self = Schedule()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.end_time = dateutil.parser.parse(json["end_time"]) 
        self.id = json["id"] 
        self.name = json["name"] 
        self.start_time = dateutil.parser.parse(json["start_time"]) 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.fixtures_ids = json["fixtures_ids"] 
        self.owner_id = json["owner_id"] 

        return self

class Session(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    expires_after int 
    id str 
    token str 
    updated_at DateTime  
    credential []str 
    owner []str 
    """

    
    
    def credential(self, db): 
        if self.credential_id != None:
            return db.get(Credential, self.credential_id)
        else:
            return None
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["expires_after"] = self.expires_after 
        json["id"] = self.id 
        json["token"] = self.token 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["credential_id"] = self.credential_id 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return SessionKind

    @staticmethod
    def unmarshal(json):
        self = Session()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.expires_after = json["expires_after"] 
        self.id = json["id"] 
        self.token = json["token"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.credential_id = json["credential_id"] 
        self.owner_id = json["owner_id"] 

        return self

class Tag(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    name str 
    updated_at DateTime  
    owner []str 
    """

    
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["name"] = self.name 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return TagKind

    @staticmethod
    def unmarshal(json):
        self = Tag()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.name = json["name"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.owner_id = json["owner_id"] 

        return self

class Task(Record):
    """ 
    completed_at DateTime 
    created_at DateTime 
    deadline DateTime 
    deleted_at DateTime 
    id str 
    name str 
    stages []Datetime 
    updated_at DateTime  
    owner []str 
    prerequisites str 
    tags str 
    """

    
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      
    
    def prerequisites(self, db): 
        [db.get(Task, id) for id in self.prerequisites_ids]
      
    
    def tags(self, db): 
        [db.get(Tag, id) for id in self.tags_ids]
      

    def marshal(self):
        json = {}

        # Traits 
        json["completed_at"] = self.completed_at.isoformat() 
        json["created_at"] = self.created_at.isoformat() 
        json["deadline"] = self.deadline.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["name"] = self.name 
        json["stages"] = [d.isoformat() for d in self.stages] 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["owner_id"] = self.owner_id 
        json["prerequisites_ids"] = self.prerequisites_ids 
        json["tags_ids"] = self.tags_ids 

        return json


    @staticmethod
    def Kind():
        return TaskKind

    @staticmethod
    def unmarshal(json):
        self = Task()

        # Traits 
        self.completed_at = dateutil.parser.parse(json["completed_at"]) 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deadline = dateutil.parser.parse(json["deadline"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.name = json["name"] 
        self.stages = map(dateutil.parser.parse, json["stages"]) 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.owner_id = json["owner_id"] 
        self.prerequisites_ids = json["prerequisites_ids"] 
        self.tags_ids = json["tags_ids"] 

        return self

class Trait(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    name str 
    primitive str 
    updated_at DateTime  
    attributes str 
    model []str 
    owner []str 
    """

    
    
    def attributes(self, db): 
        [db.get(Attribute, id) for id in self.attributes_ids]
      
    
    def model(self, db): 
        if self.model_id != None:
            return db.get(Model, self.model_id)
        else:
            return None
      
    
    def owner(self, db): 
        if self.owner_id != None:
            return db.get(User, self.owner_id)
        else:
            return None
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["name"] = self.name 
        json["primitive"] = self.primitive 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["attributes_ids"] = self.attributes_ids 
        json["model_id"] = self.model_id 
        json["owner_id"] = self.owner_id 

        return json


    @staticmethod
    def Kind():
        return TraitKind

    @staticmethod
    def unmarshal(json):
        self = Trait()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.name = json["name"] 
        self.primitive = json["primitive"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.attributes_ids = json["attributes_ids"] 
        self.model_id = json["model_id"] 
        self.owner_id = json["owner_id"] 

        return self

class User(Record):
    """ 
    created_at DateTime 
    deleted_at DateTime 
    id str 
    password str 
    updated_at DateTime  
    authorizations str 
    credentials str 
    groups str 
    sessions str 
    """

    
    
    def authorizations(self, db): 
        [db.get(Group, id) for id in self.authorizations_ids]
      
    
    def credentials(self, db): 
        [db.get(Credential, id) for id in self.credentials_ids]
      
    
    def groups(self, db): 
        [db.get(Group, id) for id in self.groups_ids]
      
    
    def sessions(self, db): 
        [db.get(Session, id) for id in self.sessions_ids]
      

    def marshal(self):
        json = {}

        # Traits 
        json["created_at"] = self.created_at.isoformat() 
        json["deleted_at"] = self.deleted_at.isoformat() 
        json["id"] = self.id 
        json["password"] = self.password 
        json["updated_at"] = self.updated_at.isoformat() 

        # Relations 
        json["authorizations_ids"] = self.authorizations_ids 
        json["credentials_ids"] = self.credentials_ids 
        json["groups_ids"] = self.groups_ids 
        json["sessions_ids"] = self.sessions_ids 

        return json


    @staticmethod
    def Kind():
        return UserKind

    @staticmethod
    def unmarshal(json):
        self = User()

        # Traits 
        self.created_at = dateutil.parser.parse(json["created_at"]) 
        self.deleted_at = dateutil.parser.parse(json["deleted_at"]) 
        self.id = json["id"] 
        self.password = json["password"] 
        self.updated_at = dateutil.parser.parse(json["updated_at"]) 

        # Relations 
        self.authorizations_ids = json["authorizations_ids"] 
        self.credentials_ids = json["credentials_ids"] 
        self.groups_ids = json["groups_ids"] 
        self.sessions_ids = json["sessions_ids"] 

        return self



