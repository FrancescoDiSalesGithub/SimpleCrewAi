import chromadb
import chromadb.api

import requests
from flask import jsonify

import duckduckgo_search

class vectorManager:

    def __init__(self,collection):
        
        self.__collection = collection
        self.__client = chromadb.PersistentClient(path="persistent.blk",settings=Settings(anonymized_telemetry=False))

    def add_or_create_data(self,data,topic,topic_id):

        collection = self.__client.get_or_create_collection(name=self.__collection)
        collection.add(documents = data,metadatas= topic,ids= topic_id)

        operation = {"operation":"concluded"}
        return jsonify(operation)

    def give_data(self,topic,query):

        collection = self.__client.get_or_create_collection(name=self.__collection)
        result = collection.query(query_texts= query,where_document={"$contains":query})
        
        return jsonify(result)

    def remove_data(self,query):
        collection = self.__client.get_or_create_collection(name=self.__collection)
        collection.delete( where_document={"$contains":str(query)})

        operation = {"operation":"concluded"}
        return jsonify(operation)

    def delete_collection(self):
        self.__client.delete_collection(name=self.__collection)

        operation = {"operation":"concluded"}
        return jsonify(operation)

    def update_data(self):
        pass


    def train(self,query,model):
        
        collection = self.__client.get_or_create_collection(name=self.__collection)
        result = collection.query(query_texts=query,where_document={"$contains":query},include=["documents"])
        
        for item in result["documents"]:
            print(item)
            knowledge_data = {"model":model,"input":item}    
            embedding_data = requests.post("http://localhost:11434/api/embeddings",json=knowledge_data)

        operation = {"operation":"concluded"}
        return jsonify(operation)


    def web_collection(self,query):
        
        collection = self.__client.get_or_create_collection(name=self.__collection)
        metadata = {"searchfrom":"web"}
        topic_id = str(query)

        duck_duck_search = duckduckgo_search.DDGS().text(query,max_results=5)

        for item in duck_duck_search:
            collection.add(documents = data,metadatas= metadata,ids= topic_id)

        operation = {"operation":"concluded"}
        return jsonify(operation)