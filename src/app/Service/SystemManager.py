import config
from src.app.Model.System import System
from src.app.Service.JsonDataParser import JsonDataParser


class SystemManager():

    def __init__(self):
        self.system = System()
        self.jsons = JsonDataParser()

    def isDbSchemaCorrect(self):
        self.dbVersion = self.system.getDbVersion()
        if self.dbVersion == config.VERSION:
            return True
        else:
            return False

    def installSchema(self):
        self.system.initDB()

    def upgradeSchema(self):
        self.system.updateDB('0.11')
        return

    def validate(self):
        while not self.isDbSchemaCorrect():
            if self.dbVersion is None:
                self.installSchema()
            elif self.dbVersion != config.VERSION:
                self.upgradeSchema()
        try:
            self.jsonsCall()
        except Exception as e:
            print(e)

    def jsonsCall(self):
        self.jsons.importFiles('malignant')
        self.jsons.importFiles('benign')