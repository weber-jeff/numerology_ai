# sign_meanings.py

# /media/jeff/numy/numerology_ai/astrology/astrology_data/sign_meanings.py

sign_definitions = {
    "Aries": {
        "keywords": ["Assertive", "Energetic", "Pioneering", "Impulsive", "Courageous"],
        "element": "Fire",
        "modality": "Cardinal",
        "ruler": "Mars",
        "symbol": "♈",
        "summary": "Aries is bold, energetic, and driven by action. A natural leader with a pioneering spirit.",
        "strengths": ["Brave", "Determined", "Confident", "Enthusiastic", "Optimistic", "Honest", "Passionate"],
        "weaknesses": ["Impatient", "Moody", "Short-tempered", "Impulsive", "Aggressive"],
    },
    "Taurus": {
        "keywords": ["Stable", "Sensual", "Practical", "Reliable", "Patient"],
        "element": "Earth",
        "modality": "Fixed",
        "ruler": "Venus",
        "symbol": "♉",
        "summary": "Taurus is grounded, sensual, and values security and comfort. Strong-willed and loyal.",
        "strengths": ["Reliable", "Patient", "Practical", "Devoted", "Responsible", "Stable"],
        "weaknesses": ["Stubborn", "Possessive", "Uncompromising"],
    },
    "Gemini": {
        "keywords": ["Communicative", "Versatile", "Curious", "Witty", "Adaptable"],
        "element": "Air",
        "modality": "Mutable",
        "ruler": "Mercury",
        "symbol": "♊",
        "summary": "Gemini is intellectual, curious, and communicative. Known for adaptability and wit.",
        "strengths": ["Gentle", "Affectionate", "Curious", "Adaptable", "Ability to learn quickly and exchange ideas"],
        "weaknesses": ["Nervous", "Inconsistent", "Indecisive"],
    },
    "Cancer": {
        "keywords": ["Nurturing", "Emotional", "Protective", "Intuitive", "Tenacious"],
        "element": "Water",
        "modality": "Cardinal",
        "ruler": "Moon",
        "symbol": "♋",
        "summary": "Cancer is nurturing, emotional, and deeply intuitive. Protective of loved ones.",
        "strengths": ["Tenacious", "Highly imaginative", "Loyal", "Emotional", "Sympathetic", "Persuasive"],
        "weaknesses": ["Moody", "Pessimistic", "Suspicious", "Manipulative", "Insecure"],
    },
    "Leo": {
        "keywords": ["Charismatic", "Generous", "Creative", "Dramatic", "Proud"],
        "element": "Fire",
        "modality": "Fixed",
        "ruler": "Sun",
        "symbol": "♌",
        "summary": "Leo is charismatic, creative, and confident. Loves to shine and inspire others.",
        "strengths": ["Creative", "Passionate", "Generous", "Warm-hearted", "Cheerful", "Humorous"],
        "weaknesses": ["Arrogant", "Stubborn", "Self-centered", "Lazy", "Inflexible"],
    },
    "Virgo": {
        "keywords": ["Analytical", "Practical", "Meticulous", "Modest", "Diligent"],
        "element": "Earth",
        "modality": "Mutable",
        "ruler": "Mercury",
        "symbol": "♍",
        "summary": "Virgo is analytical, detail-oriented, and practical. A natural helper and perfectionist.",
        "strengths": ["Loyal", "Analytical", "Kind", "Hardworking", "Practical"],
        "weaknesses": ["Shyness", "Worry", "Overly critical of self and others", "All work and no play"],
    },
    "Libra": {
        "keywords": ["Diplomatic", "Charming", "Fair-minded", "Sociable", "Artistic"],
        "element": "Air",
        "modality": "Cardinal",
        "ruler": "Venus",
        "symbol": "♎",
        "summary": "Libra is diplomatic, social, and harmony-driven. Seeks balance in all things.",
        "strengths": ["Cooperative", "Diplomatic", "Gracious", "Fair-minded", "Social"],
        "weaknesses": ["Indecisive", "Avoids confrontations", "Will carry a grudge", "Self-pity"],
    },
    "Scorpio": {
        "keywords": ["Intense", "Passionate", "Resourceful", "Mysterious", "Determined"],
        "element": "Water",
        "modality": "Fixed",
        "ruler": "Pluto",  # Traditional ruler: Mars
        "symbol": "♏",
        "summary": "Scorpio is intense, passionate, and mysterious. Values depth and transformation.",
        "strengths": ["Resourceful", "Brave", "Passionate", "Stubborn", "A true friend"],
        "weaknesses": ["Distrusting", "Jealous", "Secretive", "Violent"],
    },
    "Sagittarius": {
        "keywords": ["Optimistic", "Adventurous", "Philosophical", "Independent", "Honest"],
        "element": "Fire",
        "modality": "Mutable",
        "ruler": "Jupiter",
        "symbol": "♐",
        "summary": "Sagittarius is adventurous, optimistic, and philosophical. Loves freedom and exploration.",
        "strengths": ["Generous", "Idealistic", "Great sense of humor"],
        "weaknesses": ["Promises more than can deliver", "Very impatient", "Will say anything no matter how undiplomatic"],
    },
    "Capricorn": {
        "keywords": ["Ambitious", "Disciplined", "Practical", "Patient", "Reserved"],
        "element": "Earth",
        "modality": "Cardinal",
        "ruler": "Saturn",
        "symbol": "♑",
        "summary": "Capricorn is disciplined, ambitious, and practical. A master of long-term goals.",
        "strengths": ["Responsible", "Disciplined", "Self-control", "Good managers"],
        "weaknesses": ["Know-it-all", "Unforgiving", "Condescending", "Expecting the worst"],
    },
    "Aquarius": {
        "keywords": ["Innovative", "Independent", "Humanitarian", "Unconventional", "Intellectual"],
        "element": "Air",
        "modality": "Fixed",
        "ruler": "Uranus",  # Traditional ruler: Saturn
        "symbol": "♒",
        "summary": "Aquarius is innovative, independent, and forward-thinking. Often ahead of their time.",
        "strengths": ["Progressive", "Original", "Independent", "Humanitarian"],
        "weaknesses": ["Runs from emotional expression", "Temperamental", "Uncompromising", "Aloof"],
    },
    "Pisces": {
        "keywords": ["Compassionate", "Imaginative", "Intuitive", "Artistic", "Gentle"],
        "element": "Water",
        "modality": "Mutable",
        "ruler": "Neptune",    # Traditional ruler: Jupiter
        "symbol": "♓",
        "summary": "Pisces is dreamy, empathetic, and creative. Deeply spiritual and emotionally wise.",
        "strengths": ["Compassionate", "Artistic", "Intuitive", "Gentle", "Wise", "Musical"],
        "weaknesses": ["Fearful", "Overly trusting", "Sad", "Desire to escape reality", "Can be a victim or a martyr"],
    }
}

ruling_planets = {
    "Aries": "Mars",
    "Taurus": "Venus",
    "Gemini": "Mercury",
    "Cancer": "Moon",
    "Leo": "Sun",
    "Virgo": "Mercury",
    "Libra": "Venus",
    "Scorpio": "Pluto",  # Traditional ruler: Mars
    "Sagittarius": "Jupiter",
    "Capricorn": "Saturn",
    "Aquarius": "Uranus",  # Traditional ruler: Saturn
    "Pisces": "Neptune"    # Traditional ruler: Jupiter
}

def get_sign_meaning(sign: str) -> str:
    """Retrieves the summary meaning for a given zodiac sign."""
    return sign_definitions.get(sign, {}).get("summary", "No meaning available for this zodiac sign.")

def get_ruling_planet(sign: str) -> str:
    """Retrieves the ruling planet for a given zodiac sign."""
    return ruling_planets.get(sign, "Unknown")

def get_sign_keywords(sign: str) -> list:
    """Retrieves keywords for a given zodiac sign."""
    return sign_definitions.get(sign, {}).get("keywords", [])

def get_sign_element(sign: str) -> str:
    """Retrieves the element for a given zodiac sign."""
    return sign_definitions.get(sign, {}).get("element", "Unknown")

def get_sign_modality(sign: str) -> str:
    """Retrieves the modality for a given zodiac sign."""
    return sign_definitions.get(sign, {}).get("modality", "Unknown")

sign_definitions = {
    "Aries": "Aries is bold, energetic, and driven by action. A natural leader with a pioneering spirit.",
    "Taurus": "Taurus is grounded, sensual, and values security and comfort. Strong-willed and loyal.",
    "Gemini": "Gemini is intellectual, curious, and communicative. Known for adaptability and wit.",
    "Cancer": "Cancer is nurturing, emotional, and deeply intuitive. Protective of loved ones.",
    "Leo": "Leo is charismatic, creative, and confident. Loves to shine and inspire others.",
    "Virgo": "Virgo is analytical, detail-oriented, and practical. A natural helper and perfectionist.",
    "Libra": "Libra is diplomatic, social, and harmony-driven. Seeks balance in all things.",
    "Scorpio": "Scorpio is intense, passionate, and mysterious. Values depth and transformation.",
    "Sagittarius": "Sagittarius is adventurous, optimistic, and philosophical. Loves freedom and exploration.",
    "Capricorn": "Capricorn is disciplined, ambitious, and practical. A master of long-term goals.",
    "Aquarius": "Aquarius is innovative, independent, and forward-thinking. Often ahead of their time.",
    "Pisces": "Pisces is dreamy, empathetic, and creative. Deeply spiritual and emotionally wise."
}

def get_sign_meaning(sign: str) -> str:
    return sign_definitions.get(sign, "No meaning available for this zodiac sign.")
