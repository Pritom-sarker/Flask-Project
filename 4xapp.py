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


    
app.run(host="149.28.29.54", port=300)
