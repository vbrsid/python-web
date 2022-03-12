from flask import Flask, render_template, url_for
import requests

app=Flask(__name__,template_folder='templates')

@app.route('/')
def hello():
	requests.get("http://a-pod-2:5002")
	return render_template('dashboard.html')


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5001, debug = True)

