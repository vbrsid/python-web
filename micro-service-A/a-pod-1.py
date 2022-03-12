from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def hello():
	requests.get("http://a-pod-2:5002")
	return "welcome to the flask tutorials"


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5001, debug = True)

