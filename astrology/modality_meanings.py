# /media/jeff/numy/numerology_ai/astrology/astrology_data/modality_meanings.py

modality_definitions = {
    "Cardinal": {
        "keywords": ["Initiating", "Leading", "Action-oriented", "Enterprising", "Pioneering"],
        "description": (
            "Cardinal signs (Aries, Cancer, Libra, Capricorn) are initiators and leaders. "
            "They mark the beginning of each of the four seasons and are known for being dynamic, ambitious, and proactive. "
            "Cardinal signs bring fresh energy and are often the ones who start projects, ideas, or movements."
        ),
        "associated_signs": ["Aries", "Cancer", "Libra", "Capricorn"]
    },
    "Fixed": {
        "keywords": ["Stabilizing", "Consistent", "Persistent", "Determined", "Resolute", "Loyal"],
        "description": (
            "Fixed signs (Taurus, Leo, Scorpio, Aquarius) are stabilizers. They are loyal, consistent, and persistent, "
            "excelling at sustaining efforts and building upon what has been started. Fixed signs provide solidity and determination, "
            "but can sometimes resist change or be stubborn."
        ),
        "associated_signs": ["Taurus", "Leo", "Scorpio", "Aquarius"]
    },
    "Mutable": {
        "keywords": ["Adaptable", "Flexible", "Communicative", "Resourceful", "Versatile", "Changeable"],
        "description": (
            "Mutable signs (Gemini, Virgo, Sagittarius, Pisces) are adaptable and flexible. "
            "They are the changers and thinkers who help transition from one phase to another, often at the end of a season. "
            "Mutable signs are versatile, curious, communicative, and often very resourceful in navigating change."
        ),
        "associated_signs": ["Gemini", "Virgo", "Sagittarius", "Pisces"]
    }
}

def get_modality_meaning(modality: str) -> str:
    """Retrieves the description for a given modality."""
    return modality_definitions.get(modality, {}).get("description", "No meaning available for this modality.")

def get_modality_details(modality: str) -> dict:
    """Retrieves all details for a given modality."""
    return modality_definitions.get(modality, {"error": f"No details found for modality: {modality}"})
