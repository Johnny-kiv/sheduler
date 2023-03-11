from flask import Flask,render_template
app = Flask(__name__)
@app.route("/enter/")
def enter():
    return render_template("enter.html")
@app.route("/")
def print():
    return render_template("print.html")
app.run(host="0.0.0.0")
