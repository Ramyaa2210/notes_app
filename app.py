from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
notes = []

page = """
<!DOCTYPE html>
<html>
<head>
    <title>My Notes App - v1</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f3f4f6;
            max-width: 650px;
            margin: 50px auto;
            padding: 20px;
        }
        h1 { color: #333; }
        form, .note {
            background: white;
            padding: 18px;
            margin-bottom: 15px;
            border-radius: 10px;
        }
        input, textarea {
            width: 95%;
            padding: 10px;
            margin: 8px 0;
        }
        button {
            background: #2563eb;
            color: white;
            padding: 10px 18px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>My Notes App</h1>
    <p>Version 1 - Add and View Notes</p>

    <form method="POST" action="/add">
        <input name="title" placeholder="Note title" required>
        <textarea name="content" placeholder="Write your note..."
                  required></textarea>
        <button type="submit">Add Note</button>
    </form>

    <h2>My Notes</h2>
    {% for note in notes %}
    <div class="note">
        <h3>{{ note.title }}</h3>
        <p>{{ note.content }}</p>
    </div>
    {% else %}
    <p>No notes yet. Add your first note!</p>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(page, notes=notes)

@app.route("/add", methods=["POST"])
def add_note():
    notes.append({
        "title": request.form["title"],
        "content": request.form["content"]
    })
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
