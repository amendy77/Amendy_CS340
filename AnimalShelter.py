from pymongo import MongoClient
from bson.objectid import ObjectId


    
class AnimalShelter (object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:33930/test?authSource=AAC'%("aacuser", "aacuser"))
        self.database = self.client['AAC']
        # Complete this create method to implement the C in CRUD
    
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary
            if insert!=0:
                return True
            else:
                return False    
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
            
            # Complete this create method to implement the R in CRUD

    def read(self, criteria=None):
        if criteria is not None:
            data = self.database.animals.find(criteria,{"_id": False})
            for document in data:
                print(document)
            
        else:
            data = self.database.animals.find({},{"_id": False})
        
        return data
