from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary data store (replace with database in real-world application)
scripts = [
    {"id": 1, "name": "Script 1", "description": "First script"},
    {"id": 2, "name": "Script 2", "description": "Second script"}
]

# Generate a unique ID for new scripts
def generate_id():
    return max(script["id"] for script in scripts) + 1 if scripts else 1

# CRUD operations

# Read all scripts
@app.route('/scripts', methods=['GET'])
def get_scripts():
    return jsonify(scripts)

# Read a specific script by ID
@app.route('/scripts/<int:script_id>', methods=['GET'])
def get_script(script_id):
    script = next((script for script in scripts if script['id'] == script_id), None)
    if script:
        return jsonify(script)
    else:
        return jsonify({"error": "Script not found"}), 404

# Create a new script
@app.route('/scripts', methods=['POST'])
def create_script():
    data = request.get_json()
    new_script = {
        "id": generate_id(),
        "name": data.get('name'),
        "description": data.get('description')
    }
    scripts.append(new_script)
    return jsonify(new_script), 201

# Update a script by ID
@app.route('/scripts/<int:script_id>', methods=['PUT'])
def update_script(script_id):
    data = request.get_json()
    for script in scripts:
        if script['id'] == script_id:
            script['name'] = data.get('name')
            script['description'] = data.get('description')
            return jsonify(script)
    return jsonify({"error": "Script not found"}), 404

# Delete a script by ID
@app.route('/scripts/<int:script_id>', methods=['DELETE'])
def delete_script(script_id):
    for index, script in enumerate(scripts):
        if script['id'] == script_id:
            del scripts[index]
            return jsonify({"message": "Script deleted"})
    return jsonify({"error": "Script not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
