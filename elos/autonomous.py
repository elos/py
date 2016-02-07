from db import DB


class AbstractAgent():
    """
    db    DB
    """

    def __init__(self, db):
        self.db = db
        self.start(db.changes())

    def start(self, changes):
        raise Exception("no implemented")


class ExampleAgent(AbstractAgent):
    """ any elos agent just needs to listen to these changes """

    def start(changes):
        while True:
            change = changes.recv()

