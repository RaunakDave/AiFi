from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import socket

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://mongo:27017/dev"
mongo = PyMongo(app)
db = mongo.db


@app.route("/")
def index():
    hostname = socket.gethostname()
    return jsonify(message="Welcome to App! I am running inside {} pod!".format(hostname))


@app.route("/customers")
def get_all_customers():
    customers = db.customer.find()
    data = []
    for customer in customers:
        item = {
            "id": str(customer["_id"]),
            "customer": customer["customer"]
        }
        data.append(item)
    return jsonify(data=data)


@app.route("/customer", methods=["POST"])
def create_customer():
    data = request.get_json(force=True)
    db.customer.insert_one({"customer": data["customer"]})
    return jsonify(message="customer saved successfully!")


@app.route("/customer/<id>", methods=["PUT"])
def update_customer(id):
    data = request.get_json(force=True)["customer"]
    response = db.customer.update_one({"_id": ObjectId(id)}, {
        "$set": {"customer": data}})
    if response.matched_count:
        message = "customer updated successfully!"
    else:
        message = "No customer found!"
    return jsonify(message=message)


@app.route("/customer/<id>", methods=["DELETE"])
def delete_customer(id):
    response = db.customer.delete_one({"_id": ObjectId(id)})
    if response.deleted_count:
        message = "customer deleted successfully!"
    else:
        message = "No customer found!"
    return jsonify(message=message)


@app.route("/customers/delete", methods=["POST"])
def delete_all_customers():
    db.customer.remove()
    return jsonify(message="All customers deleted!")


@app.route("/stores")
def get_all_stores_data():
    customers = db.customer.find()
    data = {}
    for customer in customers:
        cust_name = customer["customer"]["FirstName"] + \
            " " + customer["customer"]["LastName"]
        for case in customer["customer"]["case"]:
            case_number = case["Number"]
            store_name = case["store"]["Name"]
            try:
                data[store_name].append(
                    {"cust_name": cust_name, "case_number": case_number})
            except KeyError:
                data[store_name] = [
                    {"cust_name": cust_name, "case_number": case_number}]
    return jsonify(data=data)


@app.route("/cases")
def get_all_cases_data():
    customers = db.customer.find()
    data = []
    for customer in customers:
        cust_name = customer["customer"]["FirstName"] + \
            " " + customer["customer"]["LastName"]
        for case in customer["customer"]["case"]:
            case_details = {
                "case_number": case["Number"], "StartTimeStamp": case["StartTimeStamp"], "EndTimeStamp": case["EndTimeStamp"]}
            store_name = case["store"]["Name"]
            data.append({"cust_name": cust_name,
                         "case_details": case_details, "store_name": store_name})
    return jsonify(data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
