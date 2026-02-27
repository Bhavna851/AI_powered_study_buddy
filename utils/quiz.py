def generate_quiz(text):
    sentences = text.split(".")
    quiz = []

    for i, sentence in enumerate(sentences):
        sentence = sentence.strip()
        if len(sentence.split()) > 6:
            question = f"Q{i+1}. What does this mean?\n→ {sentence}?"
            quiz.append(question)

        if len(quiz) == 5:
            break

    if not quiz:
        return "Not enough content to generate quiz."

    return "\n\n".join(quiz)