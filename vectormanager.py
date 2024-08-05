import chromadb
import chromadb.api


import requests
from flask import jsonify

from chromadb import Settings

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

    def update_data(self,ids_collection,metadata,document):
        collection = self.__client.get_or_create_collection(name=self.__collection)
        collection.update(ids=ids_collection,metadatas=metadata,documents=document)

        operation = {"operation":"concluded"}
        return jsonify(operation)
        


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
        material_to_learn = []

        for search_result in duck_duck_search:
            material_to_learn.append(search_result["body"])

        counter = 0

        for item in material_to_learn:
            ids_list = []
            
            ids_list.append(topic_id+"_"+str(counter))
            collection.add(documents = item,metadatas= metadata,ids= ids_list)

            ids_list.clear()
            counter = counter + 1

        operation = {"operation":"concluded"}
        return jsonify(operation)