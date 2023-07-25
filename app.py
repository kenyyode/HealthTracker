from flask import Flask, jsonify, request, render_template 

app = Flask(__name__)

@app.route("/")

def home():
    return jsonify(message="Welcome to the Health tracker backend")

if __name__ ==  "__main__":
    app.run(debug=True)
