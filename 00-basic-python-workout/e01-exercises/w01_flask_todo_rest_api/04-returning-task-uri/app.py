from flask import Flask, jsonify, abort, make_response, request, url_for

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
    return jsonify({"tasks": [make_public_task(task) for task in tasks]})


@app.route("/todo/api/v1/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = [task for task in tasks if task["id"] == task_id]
    if len(task) == 0:
        abort(404)

    return jsonify({"task": make_public_task(task[0])})


@app.route("/todo/api/v1/tasks", methods=["POST"])
def create_task():
    if not request.json or not "title" in request.json:
        abort(400)

    task = {
        "id": tasks[-1]["id"] + 1, # we assume the largest id number is in the last pos
        "title": request.json["title"],
        "description": request.json.get("description", "n/a"),
        "done": False
    }

    tasks.append(task)
    return jsonify({"task": make_public_task(task)}), 201

@app.route("/todo/api/v1/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = [task for task in tasks if task["id"] == task_id]
    if len(task) == 0:
        abort(404)

    if not request.json:
        abort(400)

    if "title" in request.json and isinstance(request.json["title"], str):
        abort(400)
    if "description" in request.json and isinstance(request.json["description"], str):
        abort(400)
    if "done" in request.json and isinstance(request.json["done"], bool):
        abort(400)

    task[0]["title"] = request.json.get("title", task[0]["title"])
    task[0]["description"] = request.json.get("description", task[0]["description"])
    task[0]["done"] = request.json.get("done", task[0]["done"])

    return jsonify({"task": make_public_task(task[0])})

@app.route("/todo/api/v1/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    task = [task for task in tasks if task["id"] == task_id]
    if len(task) == 0:
        abort(404)

    tasks.remove(task[0])
    return jsonify(""), 204


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not Found"}), 404)


def make_public_task(task):
    new_task = {}
    for field in task:
        if field == "id":
            new_task["uri"] = url_for("get_task", task_id=task["id"], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

if __name__ == "__main__":
    app.run(debug=True)
