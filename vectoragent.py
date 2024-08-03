import agent
import vectormanager

class vectorAgent(agent.agent):
    
    def __init__(self,name_collection,data_put,topic,topic_id):
        self.__namecollection = name_collection
        self.__dataplain = data_put
        self.__topic = topic
        self.__topicid = topic_id

    def doVector(self):
        vector = vectormanager.vectorManager(self.__namecollection)
        return vector.add_or_create_data(data=self.__dataplain,topic=self.__topic,topic_id=self.__topicid)       
         
    def getVector(self):
        vector = vectormanager.vectorManager(self.__namecollection)
        return  vector.give_data(self.__topic,self.__dataplain)

    def removeVector(self,query):
        vector = vectormanager.vectorManager(self.__namecollection)
        return vector.remove_data(query)

    def removeCollection(self):
        vector = vectormanager.vectorManager(self.__namecollection)       
        return vector.delete_collection()

    def populateWebVector(self,search_query):
        vector = vectormanager.vectorManager(self.__namecollection)
        return vector.web_collection(search_query)
        
    def updateVector(self):
        vector = vectormanager.vectorManager(self.__namecollection)
        return vector.update_data()

    def trainLLM(self,query,model):
        vector = vectormanager.vectorManager(self.__namecollection)
        return vector.train(query,model)