from flask import Flask
import random

app = Flask(__name__)

@app.route("/buy")
def hello():
	return "{}".format(['Buy XAUUSD 1708.6 1710.0 1703.0 0.01','Buy XAUUSD 0 1710.0 1703.0 0.01','sell XAUUSD 1708.6 1706.0 1713.0 0.1' ][random.randint(0,2)])



if __name__ == "__main__":
    app.run(host="149.28.29.54", port=300)
