from  elos.autonomous import AbstractAgent
from elos.db import DB
from elos.models import Event, Location

import json

from os.path import expanduser
home = expanduser("~")

with open(home + "/elosconfig.json") as config_file:
    config = json.load(config_file)

def locationString(self):
    return "(lat: %s, lon: %s, alt: %s)" % (self.latitude, self.longitude, self.altitude)

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
                print("Received '%s' %s" % (event.name, locationString(loc)))

def main():
    print("Connecting to %s with Username: %s" % (config["Host"], config["PublicCredential"]))
    # len http:// = 7 forward to splice off protocol, db doesn't expect it
    db = DB(config["Host"][7:], config["PublicCredential"], config["PrivateCredential"])
    print("This example streams events")
    MyAgent(db)

if __name__ == "__main__":
    main()
