# SimpleCrewAi
ai crew using not so much headache code

# Prerequisites

- A running ollama on your machine
- A model already pulled
- pip3
- python3 interpreter

# How to install
Run the following command in the project directory:
```
pip3 install -r requirements.txt
```

# How to run
Create a yaml file called **agent.yaml** and write the following:
```
agents:
  - name: example1
    port: 1234
  - name: example2
    port: 4567

```

After saving the file run:

```

python3 simplecrew-multiplayer.py agent.yaml /destination/path

```

wait for the run of the script and then go to the destination folder. In the destination folder you have each folder with the name of your agent, go in that directory and the run:

```
python3 agent-name.py
```
where **agent-name** is the name of your agent

# REST API Endpoint

These are the following rest api of your agent:
- /task
- /vector
- /retrievevector
- /trainvector
- /deletevector
- /deletecollection
- /populatewebvector
- /updatevector
  
## Task

The /task api accepts as http method POST and a json body like the following:
```
{

"name":"name of your agent",
"tasks":["what is the meaning of life?","who is luke skywalker?"],
"web": true,
"model": "mistral"

}

```

The web option if its value is true let the ai model to search on the internet with the help of duck duck go search engine. If it is false the model will reply locally. the response will be the reply of the ai model to the prompts.

## Vector

It inserts in the vector database some values as the following:

```
{

"collection":"name of the collection",
"prompt":["the sky is blue","donkeys can not fly"],
"topic": "obvious things",
"topic_id": ["obvious_things_id_1","obvious_things_id_2"]

}
```



The response will notify the user that the data has been inserted in the vector database

## Retrieve vector

It will search in the vector database given a specific query:

```

{

"collection":"name of the collection",
"topic": "obvious things",
"prompt": "sky"
}

```
as response will give all the data given by the prompt


## Train vector

It will train the ai model from the data stored in the vector database:

```

{

"model":"mistral",
"query": "sky",
"collection": "name of the collection"
}

```

In response the api will notify the user with the operation of adding embeddings to the ai model has been completed

# Delete vector

Deletes a vector record using a query in the collection

```

{
  "collection":"name of the collection",
  "query":"record i want to delete"
}


```

# Delete collection

Deletes a collection in the vector database

```

{
  "collection":"name of the collection"
}


```


# Populate web vector

Does a duckduckgo research and inserts the first results in the vector database

```

{
  "collection":"name of the collection",
  "query":"query to send to duck duck go search engine"
}


```

# Update vector

Updates a vector record

```

{
  "collection":"name of the collection",
  "prompt":"the prompt that you want to update",
  "topic":"the topic of the collection",
  "topic_id":"the id of the topic in the vector database"
}

```



