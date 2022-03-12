from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello():
    data = [
        {"feed": "New record, over 90 views", "mins": "10", "symbol": "user"},
        {"feed": "Database error", "mins": "15", "symbol": "bell"},
        {"feed": "New record, over 40 views", "mins": "17", "symbol": "users"},
        {"feed": "New comments", "mins": "25", "symbol": "comment"},
        {"feed": "Check transactions", "mins": "28", "symbol": "bookmark"},
        {"feed": "CPU overload", "mins": "35", "symbol": "laptop"},
        {"feed": "New shares", "mins": "39", "symbol": "share-alt"}
    ]
    return json.dumps(data)


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5002, debug = True)

