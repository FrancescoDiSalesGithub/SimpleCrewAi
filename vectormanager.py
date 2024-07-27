import chromadb
import chromadb.api

import requests
from flask import jsonify

import random

class vectorManager:

    def __init__(self,collection):
        
        self.__collection = collection
        self.__client = chromadb.PersistentClient(path="persistent.blk")

    def add_or_create_data(self,data,topic,topic_id):

        collection = self.__client.get_or_create_collection(name=self.__collection)
        collection.add(documents = data,metadatas= topic,ids= topic_id)

        done_operation = {"operation":"concluded"}
        return jsonify(done_operation)

    def give_data(self,topic,query):

        collection = self.__client.get_or_create_collection(name=self.__collection)
        result = collection.query(query_texts= query,where_document={"$contains":query})
        
        return jsonify(result)
    
    def train(self,query,model):
        
        collection = self.__client.get_or_create_collection(name=self.__collection)
        result = collection.query(query_texts=query,where_document={"$contains":query},include=["documents"])
        
        for item in result["documents"]:
            print(item)
            knowledge_data = {"model":model,"input":item}    
            embedding_data = requests.post("http://localhost:11434/api/embeddings",json=knowledge_data)

        done_operation = {"operation":"concluded"}
        return jsonify(done_operation)

    def delete_collection(self):
        self.__client.delete_collection(name=self.__collection)
        
