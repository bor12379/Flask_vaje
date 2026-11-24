from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ljubezen", methods = ["POST"])
def ljubezen():
    #print(request.form)
    i1 = request.form["ime1"]
    i2 = request.form["ime2"]
    procent = 0
    if i1.strip().lower() == "bor" or i2.strip().lower() == "bor":
        procent = random.randint(90, 100)
    else:
        procent = random.randint(0, 100)
    if i1.strip().lower() == "matej" or i2.strip().lower() == "matej":
        procent = random.randint(0, 10)
    else:
        procent = random.randint(0, 100)
    if procent < 30:
        komentar = "Pozabi"
    elif procent < 70:
        komentar = "Morda"
    else:
        komentar = "Poroka!"  
    if i1.strip().lower() == i2.strip().lower():
        samoljublje = "samoljublje"
        procent = 100
    else:
        pass
        

    
    return render_template("index.html", ime1 = i1, ime2 = i2, p = procent, komentar = komentar, samoljublje = samoljublje)

app.run(debug = True)