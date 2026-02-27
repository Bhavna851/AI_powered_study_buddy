
from flask import Flask, render_template, request
from utils.summarizer import summarize_text
from utils.notes import short_notes
from utils.quiz import generate_quiz
import PyPDF2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""

    if request.method == "POST":
        text = request.form.get("text")
        action = request.form.get("action")

        if (not text or text.strip() == "") and "pdf" in request.files:
            pdf = request.files["pdf"]
            reader = PyPDF2.PdfReader(pdf)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        if not text:
            output = "Please enter text or upload a PDF."
        else:
            if action == "summary":
                output = summarize_text(text)
            elif action == "notes":
                output = short_notes(text)
            elif action == "quiz":
                output = generate_quiz(text)

    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
