from flask import Flask

app = Flask(__name__)

@app.route("/employees")
def employees():
    return {"employees": ["marben", "dave", "pherjohn"]}

if __name__ == "__main__":
    app.run(debug=True)