import json

def findBoogity(data):
    for p in data:
        if("Boogity" in str(p["text"]) or "boogity" in str(p["text"])):
            print(p["name"] + ": " + str(p["text"]) + "\n")

def findZo(data):
    f = open("demofile2.txt", "w", encoding = 'UTF-8')
    for p in data:
        if(p["name"] == "Zo"):
            #print(p["name"] + ": " + str(p["text"]) + "\n")
            f.write(p["name"] + ": " + str(p["text"]) + "\n\n")
    
    f.close()

with open('Groupme Data/message.json', encoding = 'UTF-8') as json_file:
    data = json.load(json_file)
    #findBoogity(data)
    findZo(data)
        
        
