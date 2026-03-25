from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    str = "<h1>Daphne4NFDI</h1><p>Here is a service or software output</p>"
    return str

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
