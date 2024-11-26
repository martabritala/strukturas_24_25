from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    atbilde = requests.get("https://api.chucknorris.io/jokes/random")
    joks = atbilde.json()

    return render_template("index.html", joks = joks["value"], bilde = joks["icon_url"])

@app.route("/jschats")
def chats():
    return render_template("chats.html")

@app.route("/jschats/suutiit", methods = ["POST"])
def suutiit():
    sanemtais = request.json
    with open("chataZinas.txt", "a") as f:
        f.write(sanemtais["saturs"])
    return jsonify("OK")

if __name__ == '__main__':
    app.run(port = 5000)