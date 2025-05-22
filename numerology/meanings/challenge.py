from .utils import get_number_from_string, calculate_challenge_numbers, reduce_number, PYTHAGOREAN_MAP

challenge_meanings = {
    1: {
        "description": "Challenge 1 tests your ability to assert yourself and develop self-confidence. You may face issues with independence or leadership.",
        "advice": "Stand your ground but avoid being overly aggressive. Build inner strength calmly.",
        "master": False,
        "color": "Red",
        "vibration": "Initiating",
        "traits": ["Determined", "Courageous", "Self-reliant"],
        "strengths": ["Leadership", "Initiative", "Drive"],
        "weaknesses": ["Impulsiveness", "Stubbornness", "Impatience"],
        "business": "Overcoming self-doubt to start your own venture or lead a team.",
        "relationships": "Learning to assert your needs without dominating others.",
        "purpose": "To develop unwavering self-belief and inspire others to do the same."
    },
    2: {
        "description": "Challenge 2 highlights struggles with cooperation, patience, and sensitivity.",
        "advice": "Practice empathy and diplomacy. Avoid conflict by listening and compromising.",
        "master": False,
        "color": "Orange",
        "vibration": "Harmonizing",
        "traits": ["Tactful", "Considerate", "Peace-loving"],
        "strengths": ["Mediation", "Teamwork", "Sensitivity"],
        "weaknesses": ["Indecision", "Over-sensitivity", "Conflict avoidance"],
        "business": "Collaborating effectively in partnerships or team-based projects.",
        "relationships": "Finding balance between your needs and the needs of your partner.",
        "purpose": "To foster harmony and understanding in all your interactions."
    },
    3: {
        "description": "Challenge 3 brings difficulties in self-expression, creativity, and social interaction.",
        "advice": "Express yourself honestly and find joyful outlets. Avoid negative self-talk.",
        "master": False,
        "color": "Yellow",
        "vibration": "Expressive",
        "traits": ["Creative", "Expressive", "Optimistic"],
        "strengths": ["Communication", "Joy", "Imagination"],
        "weaknesses": ["Restlessness", "Superficiality", "Moodiness"],
        "business": "Finding creative ways to market your skills or products.",
        "relationships": "Expressing your feelings openly and honestly to your loved ones.",
        "purpose": "To inspire joy and creativity in the world through your unique self-expression."
    },
    4: {
        "description": "Challenge 4 tests discipline, responsibility, and perseverance.",
        "advice": "Embrace structure and patience. Avoid being overly rigid or pessimistic.",
        "master": False,
        "color": "Green",
        "vibration": "Foundational",
        "traits": ["Practical", "Organized", "Reliable"],
        "strengths": ["Persistence", "Focus", "Hard work"],
        "weaknesses": ["Stubbornness", "Rigidity", "Cynicism"],
        "business": "Building a solid foundation for your business through careful planning.",
        "relationships": "Committing to long-term relationships and building a stable home life.",
        "purpose": "To create lasting structures and systems that bring stability and order to the world."
    },
    5: {
        "description": "Challenge 5 involves issues with freedom, adaptability, and change.",
        "advice": "Be flexible and open to new experiences. Avoid reckless behavior.",
        "master": False,
        "color": "Turquoise",
        "vibration": "Dynamic",
        "traits": ["Adventurous", "Energetic", "Curious"],
        "strengths": ["Versatility", "Resourcefulness", "Freedom-loving"],
        "weaknesses": ["Restlessness", "Impatience", "Irresponsibility"],
        "business": "Adapting to changing market conditions and embracing innovation.",
        "relationships": "Maintaining excitement and variety in your relationships.",
        "purpose": "To explore the world and inspire others to embrace change and freedom."
    },
    6: {
        "description": "Challenge 6 deals with responsibility to others, balancing personal needs with family and community demands.",
        "advice": "Practice self-care alongside caring for others. Avoid martyrdom or over-controlling.",
        "master": False,
        "color": "Blue",
        "vibration": "Nurturing",
        "traits": ["Caring", "Responsible", "Supportive"],
        "strengths": ["Compassion", "Harmony", "Reliability"],
        "weaknesses": ["Overprotectiveness", "Anxiety", "Martyrdom"],
        "business": "Creating a business that benefits the community and supports your employees.",
        "relationships": "Balancing your needs with the needs of your family and loved ones.",
        "purpose": "To heal and support others, creating harmony and balance in your community."
    },
    7: {
        "description": "Challenge 7 tests trust, introspection, and spiritual growth.",
        "advice": "Be open to others and avoid excessive withdrawal. Cultivate trust and faith.",
        "master": False,
        "color": "Indigo",
        "vibration": "Reflective",
        "traits": ["Analytical", "Introspective", "Spiritual"],
        "strengths": ["Wisdom", "Intuition", "Focus"],
        "weaknesses": ["Isolation", "Cynicism", "Secretiveness"],
        "business": "Using your intuition and analytical skills to make sound business decisions.",
        "relationships": "Building trust and intimacy with your partner through open communication.",
        "purpose": "To uncover hidden truths and bring spiritual or intellectual insights to the world."
    },
    8: {
        "description": "Challenge 8 involves issues with power, control, and material success.",
        "advice": "Use your power responsibly and maintain integrity. Avoid greed or dominance.",
        "master": False,
        "color": "Gold",
        "vibration": "Authoritative",
        "traits": ["Ambitious", "Efficient", "Pragmatic"],
        "strengths": ["Leadership", "Organization", "Confidence"],
        "weaknesses": ["Domineering", "Materialism", "Stubbornness"],
        "business": "Using your power and resources to create a positive impact on the world.",
        "relationships": "Sharing power and control equally with your partner.",
        "purpose": "To achieve material success and use your power for good."
    },
    9: {
        "description": "Challenge 9 deals with letting go, forgiveness, and compassion.",
        "advice": "Practice forgiveness and release. Avoid bitterness or unrealistic idealism.",
        "master": False,
        "color": "Purple",
        "vibration": "Transcendent",
        "traits": ["Compassionate", "Idealistic", "Generous"],
        "strengths": ["Tolerance", "Creativity", "Empathy"],
        "weaknesses": ["Over-sensitivity", "Naivety", "Impatience"],
        "business": "Creating a business that aligns with your values and contributes to a better world.",
        "relationships": "Forgiving past hurts and moving forward with compassion.",
        "purpose": "To uplift humanity and contribute to a better world through selfless service and compassion."
    },
    11: {
        "description": "Master Challenge 11 brings intense emotional and spiritual challenges.",
        "advice": "Trust your intuition and find healthy emotional outlets. Avoid overwhelm and anxiety.",
        "master": True,
        "color": "Silver",
        "vibration": "Elevated Insight",
        "traits": ["Visionary", "Inspirational", "Sensitive"],
        "strengths": ["Intuition", "Creativity", "Empathy"],
        "weaknesses": ["Anxiety", "Emotional overwhelm", "Restlessness"],
        "business": "Using your vision and intuition to create a business that inspires others.",
        "relationships": "Connecting with your partner on a deep spiritual level.",
        "purpose": "To enlighten and inspire others with your spiritual insights."
    },
    22: {
        "description": "Master Challenge 22 tests your ability to build on large visions with discipline and realism.",
        "advice": "Stay grounded and focused. Balance ambition with patience.",
        "master": True,
        "color": "Platinum",
        "vibration": "Master Builder",
        "traits": ["Powerful", "Disciplined", "Visionary"],
        "strengths": ["Leadership", "Strategic planning", "Determination"],
        "weaknesses": ["Perfectionism", "Workaholism", "Control issues"],
        "business": "Building a large-scale business that benefits humanity.",
        "relationships": "Creating a strong and stable partnership that supports your shared vision.",
        "purpose": "To manifest your dreams into reality and create lasting structures that benefit humanity."
    },
    33: {
        "description": "Master Challenge 33 challenges you to balance spiritual service with practical needs.",
        "advice": "Practice self-care while serving others. Avoid martyrdom.",
        "master": True,
        "color": "Rose Pink",
        "vibration": "Compassionate Teacher",
        "traits": ["Compassionate", "Selfless", "Inspirational"],
        "strengths": ["Healing", "Teaching", "Empathy"],
        "weaknesses": ["Self-sacrifice", "Overwhelm", "Martyrdom"],
        "business": "Creating a business that provides healing and support to others.",
        "relationships": "Nurturing your relationships with unconditional love and compassion.",
        "purpose": "To heal and uplift humanity through selfless service and unconditional love."
    }
}
def get_challenge_analysis(number: int) -> dict:
    """Return challenge number meaning including master numbers."""
    meaning = challenge_meanings.get(number)

    if not meaning:
        return {
            "summary": "Invalid Challenge number.",
            "advice": "Please enter a valid Challenge number (1-9, 11, 22, 33).",
            "traits": [],
            "strengths": [],
            "weaknesses": [],
            "business": "N/A",
            "relationships": "N/A",
            "purpose": "N/A",
            "color": "N/A",
            "vibration": "N/A",
            "master": False
        }

    return {
        "summary": f"Challenge Number {number} - {meaning['description']}",
        "advice": meaning['advice'],
        "master": meaning['master'],
        "traits": meaning['traits'],
        "strengths": meaning['strengths'],
        "weaknesses": meaning['weaknesses'],
        "business": meaning['business'],
        "relationships": meaning['relationships'],
        "purpose": meaning['purpose'],
        "color": meaning.get('color', 'N/A'),
        "vibration": meaning.get('vibration', 'N/A'),
    }


def get_challenge_report_string(number: int) -> str:
    """Generates and returns a formatted string report for a given Challenge number."""
    analysis = get_challenge_analysis(number)

    report_string = "=" * 60 + "\n"
    report_string += f"⚔️ Challenge Number {number} Report ⚔️\n"
    report_string += "=" * 60 + "\n"
    report_string += f"🧾 Summary: {analysis['summary']}\n"
    report_string += f"💡 Advice: {analysis['advice']}\n"
    report_string += f"✨ Master Number: {'Yes' if analysis['master'] else 'No'}\n"

    if analysis['traits']:
        report_string += "\n🔑 Core Traits: " + ', '.join(analysis['traits']) + "\n"
    if analysis['strengths']:
        report_string += "✅ Strengths: " + ', '.join(analysis['strengths']) + "\n"
    if analysis['weaknesses']:
        report_string += "⚠️ Weaknesses: " + ', '.join(analysis['weaknesses']) + "\n"

    report_string += "\n💼 Business Outlook:\n"
    report_string += f" - {analysis['business']}\n"
    report_string += "\n❤️ Relationships:\n"
    report_string += f" - {analysis['relationships']}\n"
    report_string += "\n🎯 Life Purpose:\n"
    report_string += f" - {analysis['purpose']}\n"
    report_string += "\n🎨 Color Vibration: " + analysis['color'] + "\n"
    report_string += "🔊 Energy Vibration: " + analysis['vibration'] + "\n"
    report_string += "=" * 60 + "\n"

    return report_string


# Example call to test output:
print(get_challenge_report_string(5))
