from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
app = Flask(__name__)

def getCsvDataAll():
    data = { 'time': [], 'data': { 'tsmc': [],'am': [],'asml': [],'sumco': [] } }
    with open("data.csv", newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            data['time'].append(row['time'])
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
            data['time'].append(row['time'])
            data['data'][company].append(row[company])
    return data

@app.route("/getAll", methods=['GET'])
def getAll():
    data = getCsvDataAll()
    return jsonify(data)

@app.route("/getCompany", methods=['GET'])
def getCompany():
    company = request.args.get('company')
    data = getCsvData(company)
    return jsonify(data)

if __name__ == '__main__':
    CORS(app, resources={r"/*": {"origins": ["*"]}})
    app.debug = True
    app.run(host='0.0.0.0', debug=True, port=9090)