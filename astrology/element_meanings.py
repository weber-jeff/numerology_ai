# /media/jeff/numy/numerology_ai/astrology/astrology_data/element_meanings.py

element_definitions = {
    "Fire": {
        "keywords": ["Action", "Enthusiasm", "Inspiration", "Spirit", "Courage", "Impulse", "Creativity"],
        "description": (
            "Fire signs (Aries, Leo, Sagittarius) are passionate, dynamic, and temperamental. "
            "They are full of energy, enthusiasm, and creativity. Fire signs are natural leaders, "
            "often taking initiative and pushing forward without fear. They can be impulsive and quick to act, "
            "needing freedom and self-expression."
        ),
        "associated_signs": ["Aries", "Leo", "Sagittarius"]
    },
    "Earth": {
        "keywords": ["Practicality", "Stability", "Material world", "Senses", "Groundedness", "Reliability", "Patience"],
        "description": (
            "Earth signs (Taurus, Virgo, Capricorn) are grounded, practical, and reliable. "
            "They value stability and are deeply rooted in the material world. Earth signs are methodical, "
            "hardworking, and tend to build things that last. They seek security and can sometimes resist change."
        ),
        "associated_signs": ["Taurus", "Virgo", "Capricorn"]
    },
    "Air": {
        "keywords": ["Intellect", "Communication", "Social interaction", "Ideas", "Logic", "Objectivity", "Relationships"],
        "description": (
            "Air signs (Gemini, Libra, Aquarius) are intellectual, communicative, and curious. "
            "They thrive on ideas, logic, and social interaction. Air signs often think abstractly, love discussion, "
            "and seek to understand the world from many perspectives. They value connection and mental stimulation."
        ),
        "associated_signs": ["Gemini", "Libra", "Aquarius"]
    },
    "Water": {
        "keywords": ["Emotions", "Intuition", "Compassion", "Subconscious", "Sensitivity", "Imagination", "Empathy"],
        "description": (
            "Water signs (Cancer, Scorpio, Pisces) are emotional, intuitive, and deeply connected to the subconscious. "
            "They are empathetic, nurturing, and often highly creative. Water signs feel things deeply, seek emotional connection, "
            "and may struggle with emotional boundaries."
        ),
        "associated_signs": ["Cancer", "Scorpio", "Pisces"]
    }
}

def get_element_meaning(element: str) -> str:
    """Retrieves the description for a given element."""
    return element_definitions.get(element, {}).get("description", "No meaning available for this element.")

def get_element_details(element: str) -> dict:
    """Retrieves all details for a given element."""
    return element_definitions.get(element, {"error": f"No details found for element: {element}"})
