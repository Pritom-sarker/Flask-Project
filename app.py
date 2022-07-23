from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    return "Hello, World!"

if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    http_server = WSGIServer(('149.28.29.54', 2000), app)
    http_server.serve_forever()
