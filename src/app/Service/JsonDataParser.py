from src.app.Collection.MetadataCollection import MetadataCollection, Acquisition, Clinical, Creator, Dataset, Meta, Metadata, Notes, Reviewed, Tag, Unstructured
import os, json, config


class JsonDataParser:

    def __init__(self):
        self.acquisition = Acquisition()
        self.clinical = Clinical()
        self.creator = Creator()
        self.dataset = Dataset()
        self.meta = Meta()
        self.metadata = Metadata()
        self.tag = Tag()
        self.notes = Notes()
        self.unstructured = Unstructured()
        self.reviewed = Reviewed()
        self.path = config.DATA_PATH
        self.dir = None
        self.collection = MetadataCollection()

    def setBaseDir(self, dir):
        self.dir = dir



    def getFileList(self):
        self.path = os.getcwd() + self.path + self.dir + "\\description"
        files = os.listdir(self.path)
        return files

    def importFiles(self, catalog):
        insertedIDs = []
        self.setBaseDir(catalog)
        self.collection.dir = catalog
        for fileName in self.getFileList():
            file = self.path + "\\" + fileName
            metadata = json.load(open(file))
            insertedIDs.append(self.collection.parseMetadata(metadata))
        print(insertedIDs)
