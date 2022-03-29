import json
from flask import Flask,jsonify,request
app = Flask(__name__)

contacts = [
    {
        "Contact": "23453342",
        "Name": "John",
        "done": "false",
        id: "1",

    },
    {
        "Contact": "23445456",
        "Name": "Lee",
        "done": "false",
    },
    {
        "Contact": "23498949",
        "Name": "Eve",
        "done": "false",
    }

]

@app.route ("/add-data", method=["POST"])

def add_task():
    if not request.json:
        return jsonify({

            "status":"error","message":"Please provide the data for the task!"
        },400
        )
