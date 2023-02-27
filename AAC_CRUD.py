#Nick Nealeigh 2-12-2023
#CS 330 SNHU

from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class CRUD:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        #username = urllib.parse.quote_plus('accuser')
        #password = urllib.parse.quote_plus('password')
        if username and password:
            uri = "mongodb://%s:%s@localhost:47815/?authSource=AAC&authMechanism=SCRAM-SHA-1" % (username, password)
            self.client = MongoClient(uri)
            self.database = self.client['AAC']
        else:
            print("ERROR: Must supply a username and password to instantiate AnimalShelter")

#Create
    def create(self, data):
        if data is not None:
            if data:
                self.database.animals.insert(data)  # data should be dictionary
                return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
        
#Read
    def read(self, data = None):
        if data:
            animals = self.database.animals.find(data,{"_id":False})
        else:
            animals = self.database.animals.find({}, {"_id":False})
        return animals
    
#Update
    def update(self, old, new):
        try:
            result = self.database.animals.update_many(old,new)
            return dumps(self.read(old))
        except Exception as e:
            return e
        
        
#Delete
    def delete(self, delete):
        try:
            result = self.database.animals.delete_many(delete)
            return dumps(self.read(delete))
        except Exception as e:
            return e
    