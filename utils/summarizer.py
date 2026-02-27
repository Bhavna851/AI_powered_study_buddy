from transformers import pipeline

summarizer = None  # lazy loading

def summarize_text(text):
    global summarizer

    if summarizer is None:
        summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn"
        )

    if len(text.split()) < 40:
        return "Text is too short to summarize."

    summary = summarizer(
        text,
        max_length=120,
        min_length=50,
        do_sample=False
    )[0]["summary_text"]

    return summary