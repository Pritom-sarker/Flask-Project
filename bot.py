from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello Geeks!! from Google Colab"

if __name__ == "__main__":
    app.run(host="149.28.29.54", port=5000)
