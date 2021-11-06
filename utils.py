def confirm(question: str) -> bool:
    reply = None
    while reply not in ("", "y", "n"):
        reply = input(f"{question} (Y/n): ").lower()
    return (reply in ("", "y"))