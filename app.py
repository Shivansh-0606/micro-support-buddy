import json
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

#-- Load data from JSON file
def load_data():
    path = os.path.join(app.root_path, 'static', 'data', 'remedies.json')
    with open(path, 'r') as f:
        return json.load(f)

#-- API endpoint to get remedy by emotion
@app.route('/api/remedy', methods=['GET'])
def get_remedy():
    emotion = request.args.get('emotion') 
    data = load_data()
    
    #-- Find the remedy for the given emotion
    for item in data:
        if item['id'] == emotion:
            return jsonify(item)
            
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)