from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
import uuid

instance_id = uuid.uuid4().hex
app = Flask(__name__)

def getResponse(data):
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    response.headers.add('Access-Control-Allow-Private-Network', 'true')
    return response

def getCsvDataAll():
    data = { 'time': [], 'data': { 'tsmc': [],'am': [],'asml': [],'sumco': [] } }
    with open("data.csv", newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            data['time'].append(row['date'])
            data['data']['tsmc'].append(row['tsmc'])
            data['data']['am'].append(row['am'])
            data['data']['asml'].append(row['asml'])
            data['data']['sumco'].append(row['sumco'])
    return data

def getCsvData(company):
    data = { 'time': [], 'data': { company: [] } }
    with open("data.csv", newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            data['time'].append(row['date'])
            data['data'][company].append(row[company])
    return data

@app.route("/getAll", methods=['GET'])
def getAll():
    data = getCsvDataAll()
    return getResponse(data)

@app.route("/getCompany", methods=['GET'])
def getCompany():
    company = request.args.get('company')
    data = getCsvData(company)
    return getResponse(data)

@app.route("/")
def get_instance_id():
    return f"Instance ID: {instance_id}"

if __name__ == '__main__':
    # CORS(app, resources={r"/*": {"origins": ["*"]}})
    app.debug = True
    app.run(host='0.0.0.0', debug=True, port=9090)
