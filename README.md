![https://img.thedailybeast.com/image/upload/c_crop,d_placeholder_euli9k,h_1441,w_2562,x_287,y_31/dpr_1.5/c_limit,w_1600/fl_lossy,q_auto/v1555311956/Courtesy_of_HBO_2_eu3vht]

# API PROJECT
## Welcome to the ideal API to analyze the general vibe of a group chat
In this project I have created an API to store users, chat groups and messages in MongoDB to then analyze the data. You can also extract all the messages from a group chat in the form of a list. 

Since I am a big Game of Thrones fanatic the examples are done with characters of Game of Thrones and quotes by them. 

In addition, there is a component of the program that analyzes the sentiment of a specific group chat. 
In order to create to the API I used flask and then MongoDB as our database system. To carry out sentiment analysis we imported the NLTK module. 

The process is as follows: 
1. Add a user name to the database.

2. Then you create a chat and add users to it in the same line

3. Add messages to that pertain to each user to specific group chats.

4. Finally, analyze the sentiment of the group chat

## Endpoints used:

Endpoint 1. To create a user name: ['http://localhost:3000/user/create/<username>']

Endpoint 2. To create a chat and assign a user to that chat.: ['http://localhost:3000/chat/<chatname>/user/<username>']

Endpoint 3. Add message to a user in a gorup chat: ['http://localhost:3000/chat/<chatname>/user/<username>/message/<message>']

Endpoint 4. Get all message from a  group chat in the form of a list: ['http://localhost:3000/chat/<chatname>/list']

Endpoint 5. Analyse the sentiment of a group chat: ['http://localhost:3000/chat/<chatname>/sentiment']
