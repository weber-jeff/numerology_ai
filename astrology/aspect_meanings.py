aspect_meanings = {
    "Sextile": {
        "name": "Sextile",
        "meaning": "A cooperative aspect creating ease, opportunity, and potential talent. It encourages action when effort is applied to open doors.",
        "keywords": ["opportunity", "support", "flow", "growth", "curiosity", "learning"],
        "strengths": ["Creative synergy", "Optimism", "Communicative talents", "Balanced action"],
        "challenges": ["Taking blessings for granted", "Laziness", "Missed chances"],
        "spiritual_lesson": "Use grace wisely. Don’t wait too long to act — opportunities are not always eternal.",
        "relationship_effect": "Encourages supportive, light-hearted, and mutually uplifting relationships.",
        "career_effect": "Favors teaching, collaboration, design, and start-up ventures.",
        "psychological_shadow": "Complacency, procrastination, false sense of ease.",
        "archetype": "The Networker – one who creates bridges and possibilities.",
        "elemental_association": "Air (Mental and Communicative)",
        "vibration": "Opportunity Bridge",
        "ruling_planet": "Venus",
        "body_part": "Hands, arms",
        "color": "Yellow"
    },

    "Square": {
        "name": "Square",
        "meaning": "A tense aspect causing friction and challenge. Growth is forced through discomfort, resistance, and breakthroughs.",
        "keywords": ["tension", "conflict", "pressure", "growth", "urgency", "drive"],
        "strengths": ["Perseverance", "Breakthroughs", "Passion", "Productive stress"],
        "challenges": ["Anger", "Obstruction", "Defensiveness", "Crisis cycles"],
        "spiritual_lesson": "Embrace discomfort as a teacher. Let pain mold you into power.",
        "relationship_effect": "Relationships may be volatile or argumentative but transformative.",
        "career_effect": "Great for entrepreneurs, crisis managers, athletes, activists — people who thrive under pressure.",
        "psychological_shadow": "Self-sabotage, projection of blame, burnout.",
        "archetype": "The Warrior – one who grows through resistance.",
        "elemental_association": "Earth (Foundation and Struggle)",
        "vibration": "Catalyst Pressure",
        "ruling_planet": "Mars",
        "body_part": "Muscles",
        "color": "Red"
    },

    "Trine": {
        "name": "Trine",
        "meaning": "A flowing aspect indicating natural talent, grace, and alignment with purpose. Things come easily — sometimes too easily.",
        "keywords": ["harmony", "talent", "luck", "alignment", "peace", "flow"],
        "strengths": ["Confidence", "Ease", "Creative genius", "Emotional intelligence"],
        "challenges": ["Complacency", "Lack of motivation", "Taking things for granted"],
        "spiritual_lesson": "Appreciate your gifts. Use your natural flow to uplift others, not to coast.",
        "relationship_effect": "Encourages loyal, balanced, emotionally supportive relationships.",
        "career_effect": "Excellent for the arts, counseling, healing, or leadership roles where flow matters.",
        "psychological_shadow": "Entitlement, underachievement, passivity.",
        "archetype": "The Artist – one who creates with ease and beauty.",
        "elemental_association": "Water (Emotion and Flow)",
        "vibration": "Harmonic Grace",
        "ruling_planet": "Jupiter",
        "body_part": "Liver",
        "color": "Blue"
    },

    "Opposition": {
        "name": "Opposition",
        "meaning": "An aspect of polarization. It reveals externalized conflict that reflects internal imbalances. A call for integration and diplomacy.",
        "keywords": ["duality", "reflection", "projection", "polarization", "balance", "contrast"],
        "strengths": ["Self-awareness", "Negotiation", "Mature decision-making", "Seeing both sides"],
        "challenges": ["Projection", "Codependency", "External chaos"],
        "spiritual_lesson": "Learn to see yourself in others. Resolve conflict through self-integration.",
        "relationship_effect": "Often manifests as mirroring — relationships teach vital lessons but may feel draining or karmic.",
        "career_effect": "Strong in law, mediation, therapy, politics — fields requiring duality navigation.",
        "psychological_shadow": "Blame, rejection, internal dissonance.",
        "archetype": "The Mirror – one who reflects the hidden truth of duality.",
        "elemental_association": "Air/Water (Mental/Emotional tension)",
        "vibration": "Reflective Polarity",
        "ruling_planet": "Venus/Mars",
        "body_part": "Kidneys",
        "color": "Green"
    },
    "Conjunction": {
        "name": "Conjunction",
        "meaning": "A potent aspect where two or more planets merge their energies, amplifying their influence. This fusion can create focused drive or internal conflict depending on the planetary nature.",
        "keywords": ["fusion", "amplification", "focus", "power", "intensity", "identity"],
        "strengths": ["Single-minded determination", "Unified vision", "Dynamic action", "Creative ignition"],
        "challenges": ["Over-identification with traits", "Blind spots", "Lack of detachment", "Compulsion"],
        "spiritual_lesson": "Balance unity with awareness. Learn to distinguish merged energies and maintain inner clarity.",
        "relationship_effect": "Can lead to powerful attraction or controlling dynamics — relationships may feel 'fated' or all-consuming.",
        "career_effect": "Great for deep-focus careers like surgery, research, invention, or leadership. Be cautious of overwork.",
        "psychological_shadow": "Loss of individual identity, obsession, burnout.",
        "archetype": "The Alchemist – one who fuses disparate forces into   transformation.",
        "elemental_association": "Fire (Initiation and Force)",
        "vibration": "Magnetic Amplifier",
        "ruling_planet": "Depends on the planets involved",
        "body_part": "Depends on the planets involved",
        "color": "Depends on the planets involved"
    },
}

def get_aspect_analysis(aspect_name: str) -> dict:
    """Return the aspect meaning data for a given aspect name."""
    analysis_data = aspect_meanings.get(aspect_name)

    if not analysis_data:
        # Return a dictionary with default values to prevent KeyErrors in the report string function
        return {
            "name": aspect_name,
            "meaning": "N/A - Aspect information not found.",
            "keywords": [],
            "strengths": [],
            "challenges": [],
            "spiritual_lesson": "N/A",
            "relationship_effect": "N/A",
            "career_effect": "N/A",
            "psychological_shadow": "N/A",
            "archetype": "N/A",
            "elemental_association": "N/A",
            "vibration": "N/A",
            "ruling_planet": "N/A",
            "body_part": "N/A",
            "color": "N/A",
            "error": f"Invalid aspect name: {aspect_name}.",
            "recommendation": "Please enter a valid aspect name (e.g., Conjunction, Sextile, Square, Trine, Opposition)."
        }
    return analysis_data

def get_aspect_report_string(aspect_name: str) -> str:
    """Generates a formatted report string for a given aspect."""
    analysis = get_aspect_analysis(aspect_name)

    if "error" in analysis:
        return f"Error: {analysis['error']}\nRecommendation: {analysis['recommendation']}\n"

    report_string = "=" * 60 + "\n"
    report_string += f"✨ Aspect: {analysis['name']} ✨\n"
    report_string += "=" * 60 + "\n"
    report_string += f"📖 Meaning: {analysis['meaning']}\n"
    report_string += f"🔑 Keywords: {', '.join(analysis['keywords']) if analysis['keywords'] else 'N/A'}\n"
    report_string += f"💪 Strengths: {', '.join(analysis['strengths']) if analysis['strengths'] else 'N/A'}\n"
    report_string += f"챌 Challenges: {', '.join(analysis['challenges']) if analysis['challenges'] else 'N/A'}\n" # Using 챌 as a placeholder for a suitable emoji
    report_string += f"🧘 Spiritual Lesson: {analysis['spiritual_lesson']}\n"
    report_string += f"❤️ Relationship Effect: {analysis['relationship_effect']}\n"
    report_string += f"💼 Career Effect: {analysis['career_effect']}\n"
    report_string += f"👤 Psychological Shadow: {analysis['psychological_shadow']}\n"
    report_string += f"🎭 Archetype: {analysis['archetype']}\n"
    report_string += f"🜄 Elemental Association: {analysis['elemental_association']}\n" # Using 🜄 as a placeholder for a suitable emoji
    report_string += f"🔊 Vibration: {analysis['vibration']}\n"
    report_string += f"🪐 Ruling Planet: {analysis['ruling_planet']}\n"
    report_string += f"🧍 Body Part: {analysis['body_part']}\n" # Using 🧍 as a placeholder for a suitable emoji
    report_string += f"🎨 Color: {analysis['color']}\n"
    report_string += "=" * 60 + "\n"

    return report_string