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

#returns a list of members ordered by total likes given to them (member name, like count)
def likeRanking(data):    
    memberDict = getMembers()
    likesDict = dict.fromkeys(memberDict, 0) #key = userid, value = total likes for that user

    #totaling the likes for each userid
    for message in data:
        #have to check if key exists to avoid adding to nothing
        if((message["user_id"]) in likesDict.keys()):
            likesDict[message["user_id"]] += len(message["favorited_by"])
        else: 
            #if person has left the chat this will trigger, they will not have a name unless manually added in getMembers()
            likesDict[message["user_id"]] = len(message["favorited_by"])        
    
    #converting userids to names
    namesDict = {}
    for userid in likesDict:
        if(userid in memberDict.keys()): #change each userid to a name
            namesDict[memberDict[userid]] = likesDict[userid]
        else:
            #if they left the chat, can't assign a name
            namesDict[userid] = likesDict[userid]
            
    
    sortedLikes = sorted(namesDict.items(), key=lambda x: x[1], reverse=True)
    return sortedLikes
    
    '''
    file = open("Like Leaderboard.txt", "w", encoding = 'UTF-8')
    file.write("Like Leaderboard \n\n----------------- \n\n" )
    for name, likes in sortedLikes:
        file.write(name + ": " + str(likes) + "\n")
        
    file.close()
    '''

#returns a list of members ordered by their total sent messages
def messageRanking(data):
    memberDict = getMembers()
    messagesDict = dict.fromkeys(memberDict, 0) #key = userid, value = total messages from that user
    
    #totaling the messages for each userid
    for message in data:
        #have to check if key exists to avoid adding to nothing
        if((message["user_id"]) in messagesDict.keys()):
            messagesDict[message["user_id"]] += 1
        else: 
            #if person has left the chat this will trigger, they will not have a name unless manually added in getMembers()
            messagesDict[message["user_id"]] = 1
        
    #converting userids to names
    namesDict = {}
    for userid in messagesDict:
        if(userid in memberDict.keys()): #change each userid to a name
            namesDict[memberDict[userid]] = messagesDict[userid]
        else:
            #if they left the chat, can't assign a name
            namesDict[userid] = messagesDict[userid]
            
    
    sortedMessages = sorted(namesDict.items(), key=lambda x: x[1], reverse=True)
    return sortedMessages

#returns a list of members ordered by their like/message ration
def likeRatioRanking(data):
    likesDict = dict(likeRanking(data))
    messagesDict = dict(messageRanking(data))
    ratioDict = {}
    
    for name in messagesDict:
        likes = likesDict[name]
        messages = messagesDict[name]
        if(messages == 0):
            ratioDict[name] = 0
        else:
            ratioDict[name] = round(likes/messages, 3)
    
    sortedRatios = sorted(ratioDict.items(), key=lambda x: x[1], reverse=True)
    #return sortedRatios

    file = open("Like Ratio Leaderboard.txt", "w", encoding = 'UTF-8')
    file.write("Like Ratio Leaderboard \n\n-------------------- \n\n" )
    for name, likes in sortedRatios:
        file.write(name + ": " + str(likes) + "\n")
        
    file.close()


with open('Groupme Data/message.json', encoding = 'UTF-8') as json_file:
    data = json.load(json_file)
    print(likeRatioRanking(data))


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

root.mainloop()

