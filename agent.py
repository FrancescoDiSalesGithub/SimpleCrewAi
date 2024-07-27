import requests
import json
import duckduckgo_search

import vectormanager

from flask import jsonify


class agent:

    def __init__(self, name,tasks,web,model):
        self.__name = name
        self.__tasks = tasks
        self.__web = web
        self.__model = model

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name   

    def getTasks(self):
        return self.__tasks;

    def setTasks(self,taskv):
        self.__tasks = taskv

    def getWeb(self):
        return self.__web     

    def setWeb(self,webx):
        self.__web = webx

    def getModel(self):
        return self.__model

    def setModel(self,modelx):
        self.__model = modelx               

    
    def doTask(self):
        print("Following agent is running:")
        print(self.__name)
        

        for task in self.__tasks:
            
            print("prompting the following task: ")
            print(task)

            data = {'model':self.__model,'prompt':task,'stream':False}

            if self.__web is True:

                research_web = task
                duck_duck_search = duckduckgo_search.DDGS().text(research_web,max_results=5)
                material_to_learn = []

                print("retrieving from the web")
                for search_results in duck_duck_search:
                    material_to_learn.append(search_results["body"])
                    print(search_results["body"])
               
                print("learning from the web")

                for learning_item in material_to_learn:
                    knowledge_data = {"model":self.__model,"prompt":learning_item}    
                    embedding_data = requests.post("http://localhost:11434/api/embeddings",json=knowledge_data)

                print("asking to the llm")
                postData = requests.post("http://localhost:11434/api/generate",json=data)
                print(postData.text)
            
            else:
            
                postData = requests.post("http://localhost:11434/api/generate",json=data)
                print(postData.text)
            
            return postData.json()['response']

