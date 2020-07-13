from src.app import app
from src.config import PORT
from pymongo import MongoClient
from src.config import DBURL
client = MongoClient(DBURL)
print(f"Connected to db {DBURL}")
db = client.get_default_database()["dbAPI"]

@app.route("/user/create/<username>")
def createUser(username):
    info = {"Name": username, "Messages": [], "Chats":[]}
    user = db.users.insert_one(info)
    return f"Welcome {username} !"

app.run("0.0.0.0", PORT, debug=True)

