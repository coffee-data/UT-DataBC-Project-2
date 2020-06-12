from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/viz-1")
def embed():
    return render_template("viz-1.html")

if __name__ == "__main__":
    app.run(debug=True)
