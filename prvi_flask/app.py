from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
# met kocke.... random (1, 6)
@app.route("/kocka")
def about():
    return render_template("met_kocke.html", kocka = random.randint(1, 6))

@app.route("/kocka/<N>")
def about1(N):
    return render_template("met_kocke.html", kocka = random.randint(1, int(N)))

sez = [1, 2, 4]
print((sez))



app.run(debug = True)


