from flask import Flask, jsonify, request

app = Flask(__name__)
contacts = [{
    "id" : 1,
    "Contact" : "123456789",
    "Name" : "Rajesh",
    "done" : False,
}, {
    "id" : 1,
    "Contact" : "123456788",
    "Name" : "Rahul",
    "done" : False,
}]

@app.route("/")
def conact_info():
    return "Contact Info"

@app.route("/add-data", methods = ["Post"])
def add_contact():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "Please provide contact info"
        }, 400)
    contact = {
        'id': contacts[-1]['id'] + 1, 
        'title': request.json['Name'], 
        'description': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status" : "success",
        "message" : "Contact added successfully!"
    })

@app.route("/get-data")
def get_contact():
    return jsonify({
        "data" : contacts
    })

if (__name__ == "__main__"):
    app.run(debug=True)