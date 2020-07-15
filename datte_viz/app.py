from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/viz-1")
def viz1():
    return render_template("viz-1.html")

@app.route("/viz-2")
def viz2():
    return render_template("viz-2.html")

@app.route("/viz-3")
def viz3():
    return render_template("viz-3.html")

@app.route("/viz-4")
def viz4():
    return render_template("viz-4.html")


if __name__ == "__main__":
    app.run(debug=True)
