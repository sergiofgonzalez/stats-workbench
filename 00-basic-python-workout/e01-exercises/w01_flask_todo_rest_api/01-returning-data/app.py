from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, Cheese, Fruit",
        "done": False
    },
    {
        "id": 2,
        "title": "Learn Flask",
        "description": "Find and follow some tutorial on the web",
        "done": False
    }
]


@app.route("/todo/api/v1/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks})


@app.route("/todo/api/v1/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = [task for task in tasks if task["id"] == task_id]
    if len(task) == 0:
        abort(404)

    return jsonify({"task": task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not Found"}), 404)

if __name__ == "__main__":
    app.run(debug=True)
