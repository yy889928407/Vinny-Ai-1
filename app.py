from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        backend_status="Running",
        backend_host=request.host,
    )

@app.route("/status")
def status():
    return jsonify(status="running")

if __name__ == "__main__":
    app.run(debug=True)