from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", backend_status="Running")

@app.route("/status")
def status():
    return jsonify(status="running")

if __name__ == "__main__":
    app.run(debug=True)