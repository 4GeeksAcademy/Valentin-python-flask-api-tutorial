from flask import Flask, jsonify
app = Flask(__name__)
from flask import request

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body:", request_body)
    todos.append(request_body)  # Add the request body to the todos list
    return jsonify(todos)  # Return the updated todos list as JSON

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < len(todos):
        del todos[position]  # Remove the task at the specified position
        return jsonify(todos)  # Return the updated todos list as JSON
    else:
        return 'Invalid position'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
