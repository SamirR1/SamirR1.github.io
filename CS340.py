'''
Created on Mar 11, 2022

@author: samir
'''
from pymongo import MongoClient
from bson.objectid import ObjectId

class Animal_Shelter(object):
    """CRUD operations or Animal collection in MongoDB"""
    
    def __init__(self,username,password):
        #initializing the MongoClient. This helps to
        #access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:30929/AAC' % (username,password))
        self.database = self.client['AAC']
        #print("init")
    
    #create method to insert data into the animals collection
    #if data is empty an exception will be thrown.
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert(data) #data should be dictionary
            #print("create")
            if result:
                print("True")
            else:
                print("False")
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            #print("no create")
    
    #read method to view what was just inserted into the collection
    #documents stores the insert function in a list that is then
    #looped through to print out the document as you would see from mongo
    def read(self,data):
        if data is not None:
            self.database.animals.find(data,{"_id": False})
            #return self.database.animals.find(data)
            return print(self.database.animals.find(data))
            #documents = list(self.database.animals.find(data))
            #for doc in documents:
                #print("\ndoc _id:", doc)
        else:
            raise Exception("Nothing to read, because data parameter is empty")

    def update(self, data, updateData):
        if data is not None:
            documents = list(self.database.animals.find(data))
            for doc in documents:
                print("\ndoc _id:", doc)
            self.database.animals.update(data, updateData)
            self.database.animals.find(data)
            documents = list(self.database.animals.find(data))
            for doc in documents:
                print("\ndoc _id:", doc)
            #print("updated")
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            
    def delete(self, data):
        if data is not None:
            self.database.animals.remove(data)
            print(self.database.animals.remove(data))
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            
    #data = {"ObjectId" : "123", "animal_type" : "cat"}
    #create({"ObjectId" : "123", "animal_type" : "cat"})
    #read(data)
            
#AS = Animal_Shelter("aacuser", "test")
#AS.create({"ObjectId" : "123", "animal_type" : "cat"})
#AS.read({"ObjectId" : "123"})