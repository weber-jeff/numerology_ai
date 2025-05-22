# /media/jeff/numy/numerology_ai/astrology/astrology_data/moon_sign_meanings.py

# These are specific interpretations for the Moon in each sign,
# focusing on emotional nature and inner needs.
moon_in_sign_definitions = {
    "Aries": {
        "summary": "Emotionally fiery, impulsive, and independent. Needs freedom and direct emotional expression. Quick to anger, quick to forgive.",
        "needs": ["Action", "Independence", "Challenge", "Excitement"],
        "emotional_style": "Direct, spontaneous, impatient, courageous."
    },
    "Taurus": {
        "summary": "Emotionally steady, sensual, and values comfort and security. Needs stability and tangible reassurance. Slow to anger, but stubborn.",
        "needs": ["Security", "Comfort", "Stability", "Sensual pleasure", "Routine"],
        "emotional_style": "Calm, patient, possessive, pleasure-seeking, loyal."
    },
    "Gemini": {
        "summary": "Emotionally curious, expressive, and restless. Needs mental stimulation and variety in emotional expression. Can rationalize feelings.",
        "needs": ["Communication", "Variety", "Mental stimulation", "Social interaction"],
        "emotional_style": "Talkative, witty, changeable, analytical about feelings, sometimes anxious."
    },
    "Cancer": {
        "summary": "Highly emotional, nurturing, and sensitive. Needs emotional security and a sense of belonging. Deeply empathetic and protective.",
        "needs": ["Emotional security", "Home", "Family", "Nurturing", "Safety"],
        "emotional_style": "Caring, moody, intuitive, protective, retentive."
    },
    "Leo": {
        "summary": "Emotionally bold, dramatic, and proud. Needs appreciation and to express feelings generously. Warm-hearted and loyal.",
        "needs": ["Appreciation", "Affection", "Self-expression", "To be admired"],
        "emotional_style": "Warm, generous, dramatic, proud, attention-seeking."
    },
    "Virgo": {
        "summary": "Emotionally analytical, reserved, and practical. Needs order and to be helpful. Can be critical of own and others' feelings.",
        "needs": ["Order", "Usefulness", "Perfection", "Analysis", "Health"],
        "emotional_style": "Reserved, critical, helpful, modest, sometimes anxious or worrisome."
    },
    "Libra": {
        "summary": "Seeks emotional harmony, fairness, and partnership. Needs balance and pleasant interactions. Avoids conflict.",
        "needs": ["Harmony", "Partnership", "Beauty", "Fairness", "Social connection"],
        "emotional_style": "Diplomatic, charming, indecisive, peace-loving, relationship-oriented."
    },
    "Scorpio": {
        "summary": "Emotionally intense, private, and transformative. Needs deep connection and control. Passionate and perceptive.",
        "needs": ["Intensity", "Transformation", "Emotional depth", "Control", "Privacy"],
        "emotional_style": "Passionate, secretive, perceptive, resilient, sometimes suspicious or jealous."
    },
    "Sagittarius": {
        "summary": "Emotionally free-spirited, optimistic, and philosophical. Needs freedom and adventure. Honest and direct with feelings.",
        "needs": ["Freedom", "Adventure", "Truth", "Optimism", "Meaning"],
        "emotional_style": "Enthusiastic, independent, restless, frank, jovial."
    },
    "Capricorn": {
        "summary": "Emotionally controlled, stoic, and ambitious. Needs achievement and respect. Can appear reserved or cool.",
        "needs": ["Respect", "Achievement", "Structure", "Control", "Security"],
        "emotional_style": "Reserved, disciplined, responsible, cautious, sometimes pessimistic."
    },
    "Aquarius": {
        "summary": "Emotionally detached, idealistic, and intellectual. Needs freedom and friendship. Values humanitarianism.",
        "needs": ["Freedom", "Individuality", "Friendship", "Intellectual connection", "Humanitarian causes"],
        "emotional_style": "Detached, friendly, unconventional, intellectual about feelings, sometimes aloof."
    },
    "Pisces": {
        "summary": "Deeply empathetic, dreamy, and emotionally fluid. Needs compassion and spiritual connection. Highly imaginative and sensitive.",
        "needs": ["Compassion", "Spiritual connection", "Imagination", "Escape", "Healing"],
        "emotional_style": "Sensitive, intuitive, artistic, escapist, self-sacrificing."
    }
}

def get_moon_in_sign_meaning(moon_sign: str) -> str:
    """Retrieves the summary meaning for the Moon in a given zodiac sign."""
    return moon_in_sign_definitions.get(moon_sign, {}).get("summary", "Unknown moon sign interpretation.")

def get_moon_in_sign_details(moon_sign: str) -> dict:
    """Retrieves all details for the Moon in a given zodiac sign."""
    return moon_in_sign_definitions.get(moon_sign, {"error": f"No details found for Moon in {moon_sign}"})
