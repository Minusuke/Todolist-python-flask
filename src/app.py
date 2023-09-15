from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
]

# GET TODOS

@app.route('/todos', methods=['GET'])
def hello_world():
    text_json = jsonify(todos)
    return text_json

# POST TODOS

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    text_json = jsonify(todos)
    return text_json

# DELETE TODOS

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position-1)
    text_json = jsonify(todos)
    return text_json 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)