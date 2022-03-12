from flask import Flask, render_template, url_for
import requests, json

app=Flask(__name__,template_folder='templates')

@app.route('/')
def hello():
    resp_data=requests.get("http://a-pod-2:5002")
    print("json:", flush=True)
    print(resp_data.json(), flush=True)
    data = json.loads(resp_data.content)
    return render_template('dashboard.html', data = data)


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5001, debug = True)

