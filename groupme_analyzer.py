import json
import tkinter as tk
#import groupme_analyzer




#returns a dict where key is user id and value is member name
def getMembers():
    with open('Groupme Data/conversation.json', encoding = 'UTF-8') as json_file:
        data = json.load(json_file)
        memberDict = {}
        
        for member in data["members"]:
            memberDict[member["user_id"]] = member["name"]
            
        '''
        this is everyone who was left the chat (not tracked in conversation.json)
        will format to make it look nice later
        '''
        memberDict['system'] = 'system'
        memberDict['calendar'] = 'calendar'
        memberDict['41177188'] = "Alejandro Carrera"
        memberDict['42316630'] = 'Andrew Dagher'
        memberDict['28473430'] = 'Liam Fitzpatrick'
        memberDict['67340809'] = 'Jordan Sheetz'
        memberDict['51541107'] = 'Dan' #shaun guy
        memberDict['809887'] = 'Dankbot'
        memberDict['63293365'] = 'Dominic Cotner'
        memberDict['30264445'] = 'Vince Luu'
        memberDict['14957604'] = 'Shawn'
        memberDict['48361256'] = 'Andrew Rafferty'
        memberDict['685'] = 'IFTTT via Jacob Weisgal'
        memberDict['28205677'] = 'Khryke'
        memberDict['28436164'] = 'Nick Guevara'
            
        return memberDict

#prints every message containing boogity
def findBoogity(data):
    for message in data:
        if("Boogity" in str(message["text"]) or "boogity" in str(message["text"])):
            print(message["name"] + ": " + str(message["text"]) + "\n\n")

#finds every message from Zo and saves it in a txt file
def findZo(data):
    file = open("zo.txt", "w", encoding = 'UTF-8')
    for message in data:
        if(message["name"] == "Zo"):
            #print(p["name"] + ": " + str(p["text"]) + "\n")
            file.write(message["name"] + ": " + str(message["text"]) + "\n\n")
    
    file.close()

#prints the most liked message(s) of all time
def mostLiked(data):
    maxLikes = 0
    maxMessages = []
    
    for message in data:
        if(len(message["favorited_by"]) == maxLikes):
            maxMessages.append(message["name"] + ": " + str(message["text"]))
        elif(len(message["favorited_by"]) > maxLikes):
            maxMessages = [message["name"] + ": " + str(message["text"])]
            maxLikes = len(message["favorited_by"])
    
    print(str(maxMessages) + "\n" + "Likes: " + str(maxLikes))

#prints a list of members ordered by total likes given to them
def likeRanking(data):    
    memberDict = getMembers()
    likesDict = dict.fromkeys(memberDict, 0) #key = userid, value = total likes for that user

    #totaling the likes for each userid
    for message in data:
        #have to check if key exists to avoid adding to nothing
        if((message["user_id"]) in likesDict.keys()):
            likesDict[message["user_id"]] += len(message["favorited_by"])
    
    #converting userids to names
    namesDict = {}
    for userid in likesDict:
        #print(userid)
        if(userid in memberDict.keys()): #change each userid to a name
            namesDict[memberDict[userid]] = likesDict[userid]
        else:
            print(userid)
            
    
    sortedLikes = sorted(namesDict.items(), key=lambda x: x[1], reverse=True)
    #print(sortedLikes)
    
    file = open("Like Leaderboard.txt", "w", encoding = 'UTF-8')
    file.write("Like Leaderboard \n\n----------------- \n\n" )
    for name, likes in sortedLikes:
        file.write(name + ": " + str(likes) + "\n")
        
    file.close()
            

with open('Groupme Data/message.json', encoding = 'UTF-8') as json_file:
    data = json.load(json_file)
    #mostLiked(data)


'''
Root Window Settings
'''
root = tk.Tk()
root.title("GroupMe Analyzer")
root.minsize(300,300)
root.geometry("800x800")

'''
Label Settings
'''
titleLabel = tk.Label(root, text="GroupMe Analyzer", font=("Courier", 44))
titleLabel.pack()

'''
Button Settings
'''


#need to use classes to get return values from functions

root.mainloop()
        
