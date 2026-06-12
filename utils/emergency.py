EMERGENCY_KEYWORDS = [
    "chest pain",
    "heart attack",
    "difficulty breathing",
    "unconscious",
    "stroke",
    "severe bleeding",
    "seizure",
    "not breathing",
    "cardiac arrest",
    "suicide",
    "overdose"
]

def check_emergency(text):
    text = text.lower()

    for keyword in EMERGENCY_KEYWORDS:
        if keyword in text:
            return True

    return False