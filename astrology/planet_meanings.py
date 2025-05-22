# /media/jeff/numy/numerology_ai/astrology/astrology_data/planet_meanings.py

planet_definitions = {
    "Sun": {
        "keywords": ["Identity", "Ego", "Vitality", "Self-expression", "Consciousness", "Willpower", "Purpose"],
        "role": "The core self, life force, creative energy, and the will to be.",
        "motivation": "To shine, to express individuality, to be recognized, to create.",
        "archetype": "The Hero, The King/Queen, The Performer"
    },
    "Moon": {
        "keywords": ["Emotions", "Instincts", "Subconscious", "Nurturing", "Inner self", "Habits", "Security", "Reactions"],
        "role": "The emotional nature, habitual responses, need for comfort, and the receptive principle.",
        "motivation": "To feel secure, to nurture and be nurtured, to connect emotionally, to belong.",
        "archetype": "The Mother, The Child, The Caregiver"
    },
    "Mercury": {
        "keywords": ["Communication", "Intellect", "Reason", "Learning", "Thought processes", "Adaptability", "Language", "Logic"],
        "role": "The mind, how one thinks, learns, processes information, and communicates.",
        "motivation": "To understand, to learn, to exchange information, to connect mentally, to articulate.",
        "archetype": "The Messenger, The Scribe, The Trickster, The Student"
    },
    "Venus": {
        "keywords": ["Love", "Beauty", "Harmony", "Relationships", "Values", "Art", "Pleasure", "Attraction", "Social grace"],
        "role": "What one values, how one relates to others, sense of aesthetics, sources of pleasure, and ability to attract.",
        "motivation": "To love and be loved, to create harmony and beauty, to appreciate, to relate.",
        "archetype": "The Lover, The Artist, The Diplomat"
    },
    "Mars": {
        "keywords": ["Action", "Energy", "Desire", "Aggression", "Courage", "Initiative", "Passion", "Drive", "Assertion"],
        "role": "The drive to act, assert oneself, pursue desires, and confront challenges.",
        "motivation": "To achieve, to conquer, to express energy, to survive, to initiate.",
        "archetype": "The Warrior, The Pioneer, The Competitor"
    },
    "Jupiter": {
        "keywords": ["Expansion", "Luck", "Optimism", "Wisdom", "Higher learning", "Abundance", "Philosophy", "Faith", "Generosity"],
        "role": "The principle of growth, opportunity, understanding, and benevolence.",
        "motivation": "To grow, to explore, to find meaning, to believe, to share.",
        "archetype": "The Sage, The Benefactor, The Explorer, The Teacher"
    },
    "Saturn": {
        "keywords": ["Structure", "Discipline", "Responsibility", "Limitations", "Lessons", "Karma", "Time", "Authority", "Fear", "Mastery"],
        "role": "The principle of limitation, structure, reality, and maturation. The great teacher.",
        "motivation": "To build, to achieve mastery through effort, to face reality, to fulfill duties, to establish boundaries.",
        "archetype": "The Elder, The Disciplinarian, The Architect, The Hermit"
    },
    "Uranus": {
        "keywords": ["Innovation", "Rebellion", "Sudden change", "Originality", "Freedom", "Technology", "Humanitarianism", "Awakening", "Individuality"],
        "role": "The catalyst for change, insight, revolution, and breakthroughs.",
        "motivation": "To be free, to innovate, to break from convention, to awaken to new possibilities.",
        "archetype": "The Revolutionary, The Inventor, The Awakener, The Eccentric"
    },
    "Neptune": {
        "keywords": ["Illusion", "Dreams", "Spirituality", "Compassion", "Intuition", "Escapism", "Arts", "Deception", "Boundlessness", "Imagination"],
        "role": "The principle of transcendence, imagination, empathy, and the unseeable.",
        "motivation": "To transcend the material, to connect spiritually, to dream, to heal, to dissolve boundaries.",
        "archetype": "The Mystic, The Dreamer, The Artist, The Healer"
    },
    "Pluto": {
        "keywords": ["Transformation", "Power", "Death & Rebirth", "Intensity", "Subconscious forces", "Regeneration", "Control", "Obsession", "Depth"],
        "role": "The agent of deep change, power, elimination, and regeneration.",
        "motivation": "To transform, to empower or be empowered, to uncover hidden truths, to eliminate what is outworn, to delve deep.",
        "archetype": "The Transformer, The Shaman, The Detective, The Phoenix"
    },
    "Chiron": {
        "keywords": ["Wound", "Healing", "Maverick", "Teacher", "Bridge", "Holism"],
        "role": "The 'Wounded Healer,' representing our deepest wound and our efforts to heal it in ourselves and others, bridging spirit and matter.",
        "motivation": "To heal, to integrate, to teach from experience, to find wholeness.",
        "archetype": "The Wounded Healer, The Mentor, The Shaman"
    },
    "TrueNode": { # North Node
        "keywords": ["Destiny", "Soul's Path", "Growth", "Evolution", "Life Lessons", "Purpose"],
        "role": "The karmic path forward, indicating qualities and experiences the soul needs to develop in this lifetime for evolution.",
        "motivation": "To evolve, to fulfill one's higher purpose, to embrace growth.",
        "archetype": "The Seeker (of one's path)"
    }
    # You can add South Node (TrueNode - 180 degrees, or swe.MEAN_NODE and its opposite)
    # Lilith (Mean Apogee - swe.MEAN_APOG), Part of Fortune, etc.
}

def get_planet_meaning(planet: str) -> str:
    """Retrieves a general role/meaning for a given planet."""
    return planet_definitions.get(planet, {}).get("role", "No meaning available for this planet.")

def get_planet_keywords(planet: str) -> list:
    """Retrieves keywords for a given planet."""
    return planet_definitions.get(planet, {}).get("keywords", [])
