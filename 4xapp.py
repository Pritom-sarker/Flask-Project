from flask import Flask
from telethon import TelegramClient, events, sync
app = Flask(__name__)
def get_query():
    f = open('query.txt', 'r')
    query = f.read()
    f.close()
    return query



@app.route("/buy")
def create_order():
	return get_query()


    
app.run( port=5000, debug=True)
