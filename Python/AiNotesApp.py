from flask import Flask, request, render_template_string
from transformers import pipeline

app = Flask(__name__)

# Initialize the summarization model
summarizer = pipeline("summarization")

notes = []

# HTML template for the notes app
template = """
<!doctype html>
<html>
<head><title>AI Notes App</title></head>
<body>
    <h1>AI Notes App</h1>
    <form method="post">
        <textarea name="note" rows="4" cols="50" placeholder="Enter your note here..."></textarea><br>
        <button type="submit">Add Note</button>
    </form>
    <h2>Notes</h2>
    <ul>
        {% for note in notes %}
            <li>{{ note }}</li>
        {% endfor %}
    </ul>
    <h2>Summarized Note</h2>
    <form method="post" action="/summarize">
        <textarea name="summary_note" rows="4" cols="50" placeholder="Enter note to summarize..."></textarea><br>
        <button type="submit">Summarize Note</button>
    </form>
    {% if summary %}
        <p>Summary: {{ summary }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        note = request.form["note"]
        if note:
            notes.append(note)
    return render_template_string(template, notes=notes, summary=None)

@app.route("/summarize", methods=["POST"])
def summarize():
    summary_note = request.form["summary_note"]
    if summary_note:
        summary = summarizer(summary_note, max_length=50, min_length=25, do_sample=False)[0]['summary_text']
        return render_template_string(template, notes=notes, summary=summary)
    return render_template_string(template, notes=notes, summary=None)

if __name__ == "__main__":
    app.run(debug=True)
