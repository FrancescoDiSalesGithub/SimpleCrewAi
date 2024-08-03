import agent
import vectoragent

import os
from flask import Flask,request,jsonify
import yaml

app = Flask(__name__)

# first use section

@app.route("/")
def welcome_back_end():
    return "<h1>Welcome to simple crew ai</h1>"

@app.route("/task",methods=['POST'])
def agents():

        json_data = request.json
        name_agent = json_data.get('name')
        tasks_agent = json_data.get('tasks')
        web_agent = json_data.get('web')
        model_agent = json_data.get('model')
        rest_agent = agent.agent(name=name_agent,tasks=tasks_agent,web=web_agent,model=model_agent)
          
        output = {"response":rest_agent.doTask()}   
        return jsonify(output)

# vector section

@app.route("/vector",methods=['POST'])
def vectordb():
    json_data = request.json
    collection = json_data.get('collection')
    vector_data = json_data.get('prompt')
    topic = json_data.get('topic')
    topic_id = json_data.get('topic_id')

    vector_agent = vectoragent.vectorAgent(name_collection=collection,data_put=vector_data,topic=topic,topic_id=topic_id)
    return vector_agent.doVector()

@app.route("/retrievevector",methods=['POST'])
def localvector(): 
    json_data = request.json
    collection = json_data.get('collection')
    topic_data = json_data.get('topic')
    vector_data = json_data.get('prompt')

    vector_agent = vectoragent.vectorAgent(name_collection=collection,data_put=vector_data,topic=topic_data,topic_id=None)
    return vector_agent.getVector()

@app.route("/deletevector",methods=['POST'])
def remove_vector_data():
    json_data = request.json
    collection = json_data.get('collection')
    query = json_data.get('query')

    if query is None:
        operation = {"operation":"not concluded","error":"The query passed has no value"}
        return jsonify(operation)

    vector_agent = vectoragent.vectorAgent(name_collection=collection,data_put=None,topic=None,topic_id=None)
    return vector_agent.removeVector(query)

@app.route("/deletecollection",methods=['POST'])
def remove_collection():
    json_data = request.json
    collection = json_data.get('collection')

    if collection is None:
        operation = {"operation":"not concluded","error":"The query passed has no value"}
        return jsonify(operation)        

    vector_agent = vectoragent.vectorAgent(name_collection=collection,data_put=None,topic=None,topic_id=None)
    return vector_agent.removeCollection()


@app.route("/populatewebvector",methods=['POST'])
def populate_web_vector():
    json_data = request.json
    collection = json_data.get('collection')
    search_term = json_data.get('query')

    vector_agent = vectoragent.vectorAgent(name_collection=collection,data_put=None,topic=None,topic_id=None)
    vector_agent.populateWebVector(search_term) 

@app.route("/updatevector",methods=['POST']):
    json_data = request.json
    collection = json_data.get('collection')
    vector_data = json_data.get('prompt')
    topic = json_data.get('topic')
    topic_id = json_data.get('topic_id')

    vector_agent = vectoragent.vectorAgent(name_collection=collection,data_put=vector_data,topic=topic,topic_id=topic_id)
    return vector_agent.updateVector()

# train section

@app.route("/trainvector",methods=['POST'])
def train_with_vector():
    json_data = request.json
    model = json_data.get('model')
    query = json_data.get('query')
    collection = json_data.get('collection')

    vector_agent = vectoragent.vectorAgent(name_collection=collection,data_put=None,topic=None,topic_id=None)
    vector_agent.trainLLM(query,model)

    return vector_agent.trainLLM(query,model)


if __name__ == '__main__':
    app.run(port={PORT})
    


