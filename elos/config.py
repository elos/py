import json
from os.path import expanduser
from elos.db import DB

home = expanduser("~")
defaultConfigPath = home + "/elosconfig.json"

class Config:
    """
    host                string
    public_credential   string
    private_credential  string
    user_id             string
    """

    def db(self):
        return DB(
            self.host[7:],
            self.public_credential,
            self.private_credential
        )


    @staticmethod
    def load(path=defaultConfigPath):
        with open(path) as config_file:
                config = json.load(config_file)

        self = Config()
        self.host = config["Host"]
        self.public_credential = config["PublicCredential"]
        self.private_credential = config["PrivateCredential"]
        self.user_id = config["UserID"]
        return self
