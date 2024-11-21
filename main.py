from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    atbilde = requests.get("https://api.chucknorris.io/jokes/random")
    joks = atbilde.json()
    atbilde = requests.get("https://api.chucknorris.io/jokes/categories")
    kategorijas = atbilde.json()
    # print(kategorijas)
    if request.method == "POST" :
        kategorija = request.form["kat"]
        print(kategorija)
        atbilde = requests.get(f"https://api.chucknorris.io/jokes/random?category={kategorija}")
        joks = atbilde.json()
    return render_template("index.html", joks = joks["value"], bilde = joks["icon_url"], kategorijas = kategorijas)

@app.route("/uni")
def uni():
    atbilde = requests.get("http://universities.hipolabs.com/search?country=latvia")
    visas = atbilde.json()
    print(visas[3]["web_pages"][0])
    nosaukumi = []
    for elements in visas:
        pieliekamais = {
            "nosaukums" : elements["name"],
            "majaslapas" : elements["web_pages"]
        }
        nosaukumi.append(pieliekamais)

    return render_template("universitates.html", uni=nosaukumi)



if __name__ == '__main__':
    app.run(port = 5000)