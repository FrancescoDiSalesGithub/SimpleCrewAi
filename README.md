# SimpleCrewAi
ai crew using not so much headache code

# How to run
Create a yaml file called **agent.yaml** and write the following:
```
agents:
  - name: example1
    port: 1234
  - name: example2
    port: 4567

```

After saving the file run **python3 simplecrew-multiplayer.py agent.yaml /destination/pth** wait for the run of the script and then go to the destination folder. In the destination folder you have each folder with the name of your agent, go in that directory and the run:

```
python3 agent-name.py
```
where **agent-name** is the name of your agent


