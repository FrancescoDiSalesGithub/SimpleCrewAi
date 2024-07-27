import yaml
import os
import chunky
import base64
import sys

try:
    if sys.argv[1] == None:
        print("USAGE: python3 mycrew-multiplayer.yml [PATH yaml file] [Path to put the ai agents]")
except Exception as usage_exception:
    print("USAGE: python3 mycrew-multiplayer.yml [PATH yaml file] [Path to put the ai agents]")
    exit(-1)

with (open(sys.argv[1],"r")) as yaml_file:
    
    yaml_decoded = yaml.safe_load(yaml_file)


    for agents_item in yaml_decoded["agents"]:

        try:
            print("making folders for agent " + agents_item['name'])
            os.mkdir(sys.argv[2] +str(agents_item['name']))
            os.chdir(sys.argv[2] +str(agents_item['name']))
        except Exception as e:
            print("agent name already exist replacing configurations only")
            os.chdir(sys.argv[2]+str(agents_item['name']))

        source_code = str(base64.b64decode(chunky.get_base_64()).decode("utf-8"))    
        source_code_port_replace = source_code.replace("{PORT}",str(agents_item["port"]))

        agent_code = base64.b64decode(chunky.put_agent()).decode("utf-8")
        vector_code = chunky.vectoragent()
        vector_manager_code = chunky.vectormanager()

        with(open(str(agents_item['name'])+".py","w")) as file_agent:
            file_agent.write(source_code_port_replace)

        with(open(str("agent.py"),"w")) as support_agent:
            support_agent.write(agent_code)

        with(open("vectormanager.py","w")) as vector_manager:
            vector_manager.write(vector_manager_code)

        with(open("vectoragent.py","w")) as vector_agent:
            vector_agent.write(vector_code)        

        os.chdir("../")
