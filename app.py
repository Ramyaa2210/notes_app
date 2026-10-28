
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

notes = [
    {"id": 1, "title": "Tasks", "content": "Agile assessment"}
]
next_id = 2

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>My Notes App - v2</title>
    <style>
        body { font-family: Arial; background: #f3f4f6; max-width: 650px; margin: 50px auto; padding: 20px; }
        form, .note { background: white; padding: 18px; margin-bottom: 15px; border-radius: 10px; }
        input, textarea { box-sizing: border-box; width: 100%; padding: 10px; margin: 8px 0; }
        button { background: #2563eb; color: white; padding: 10px 18px; border: none; border-radius: 5px; cursor: pointer; }
        a { margin-right: 10px; }
    </style>
</head>
<body>
    <h1>My Notes App</h1>
    <p>Version 2 - Add, View and Edit Notes</p>

    <form method="POST" action="/add">
        <input name="title" placeholder="Note title" required>
        <textarea name="content" placeholder="Write your note..." required></textarea>
        <button type="submit">Add Note</button>
    </form>

    <h2>My Notes</h2>
    {% for note in notes %}
    <div class="note">
        {% if edit_id == note.id %}
        <form method="POST" action="/edit/{{ note.id }}">
            <input name="title" value="{{ note.title }}" required>
            <textarea name="content" required>{{ note.content }}</textarea>
            <button type="submit">Save Changes</button>
            <a href="/">Cancel</a>
        </form>
        {% else %}
        <h3>{{ note.title }}</h3>
        <p>{{ note.content }}</p>
        <a href="/?edit={{ note.id }}">Edit</a>
        {% endif %}
    </div>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def index():
    edit_id = request.args.get("edit", type=int)
    return render_template_string(HTML, notes=notes, edit_id=edit_id)

@app.route("/add", methods=["POST"])
def add():
    global next_id
    notes.append({
        "id": next_id,
        "title": request.form["title"],
        "content": request.form["content"]
    })
    next_id += 1
    return redirect("/")

@app.route("/edit/<int:note_id>", methods=["POST"])
def edit(note_id):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = request.form["title"]
            note["content"] = request.form["content"]
            break
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
