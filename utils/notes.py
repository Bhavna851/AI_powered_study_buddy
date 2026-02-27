def short_notes(text):
    lines = text.split(".")
    notes = []

    for line in lines:
        line = line.strip()
        if len(line) > 30:
            notes.append("• " + line)

    if not notes:
        return "Not enough content to create short notes."

    return "\n".join(notes[:6])