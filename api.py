from src.app import app
from src.config import PORT
from pymongo import MongoClient
from src.config import DBURL
client = MongoClient(DBURL)
from errorHelper import errorHelper, Error404, APIError
from bson.json_util import dumps

print(f"Connected to db {DBURL}")
db = client.get_default_database()["dbAPI"]


@app.route("/")
def first_page():
    return 'Hello, user! Welcome to my Messenger API.'

@errorHelper
@app.route("/user/create/<username>")
def createUser(username):
    info = {"Name": username, "Messages": [], "Chats":[]}
    user = db.users.insert_one(info)
    return f'Welcome {username}!'
@errorHelper
@app.route("/chat/<chatname>/user/<username>")
def chatCreate(chatname,username):
    data = db.users.find({'Name': username},{'_id':0})
    output= []
    if data.count() == 0:
        raise Error404(f'This user is not registered.')
    else:
        query = db.unique.find({'$and': [{'Name': username},{'Chats': [chatname]}]},{'_id':0})
        if query.count() == 0:
            output =  db.users.update({'Name': username},{'$set':{'Chats': [chatname]}})
            return f'Hello, {username} the new chat "{chatname}" is Created!'
        else:
            return f"Error: User already in the chat."

#Adding messages to chat 
@app.route('/chat/<chatname>/user/<username>/message/<message>')
@errorHelper
def chatAddMessage(chatname, username, message):
    if db.users.count_documents({'Name': username,'Chats': [chatname]}) == 0:
        raise Error404 (f'This user is not registered.')
    else:
        db.users.update({'Name': username},{'$set':{"Messages": [message]}})
        return f'Thank you for your message!'


# Get all message from chat 
@app.route('/chat/<chatname>/list')
@errorHelper
def chatList(chatname):
    output = []
    if db.users.count({'Chats': chatname}) == 0:
        raise Error404 (f'This chat is not registered.')
    else:
        data = list(db.users.find({ 'Chats': chatname },{'_id':0,'Messages':1}))
        list1=[]
    for item in data:
        for message, sentence in item.items():
            if sentence != "":
                list1.append(sentence)      
    flat_list = [item for sublist in list1 for item in sublist]
    return dumps(flat_list)

app.run("0.0.0.0", PORT, debug=True)

