from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    atbilde = requests.get("https://api.chucknorris.io/jokes/random")
    joks = atbilde.json()

    return render_template("index.html", joks = joks["value"], bilde = joks["icon_url"])

if __name__ == '__main__':
    app.run(port = 5000)