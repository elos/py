from  elos.autonomous import AbstractAgent
from elos.db import DB
from elos.models import Event

"""
    Example of an agent watching the elos ontology,
    printing new events in the system
"""
class MyAgent(AbstractAgent):
    def start(self, changes):
        while True:
            change = changes.recv()

            if change.record_kind == "event":
                event = change.record_data.unmarshal(Event)
                loc = event.location(self.db)
                print("Received '%s' %s" % (event.name, loc.string()))

def main():
    db = DB("elos.pw:8080", "public", "private")
    MyAgent(db)

if __name__ == "__main__":
    main()