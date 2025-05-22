import sys
import os

# Add the project root to the Python path if running as a top-level script
if __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

from .utils import reduce_number, get_reduced_date_components

pinnacle_meanings = {
    1: {
        "description": "Pinnacle 1 is a time of new beginnings, independence, and leadership. You’re called to step up, take charge, and assert your individuality.",
        "advice": "Be confident and proactive. Take initiative, but avoid impatience or stubbornness.",
        "master": False,
        "traits": ["Independent", "Ambitious", "Courageous"],
        "strengths": ["Leadership", "Innovation", "Determination"],
        "weaknesses": ["Impulsiveness", "Stubbornness", "Aggression"],
        "business": "Starting your own business or taking on a leadership role.",
        "relationships": "Focusing on personal growth and establishing independence.",
        "purpose": "To develop self-reliance and lead with courage."
    },
    2: {
        "description": "Pinnacle 2 focuses on relationships, diplomacy, and cooperation. This period encourages patience and harmony.",
        "advice": "Cultivate teamwork and diplomacy. Avoid being overly sensitive or passive.",
        "master": False,
        "traits": ["Diplomatic", "Supportive", "Tactful"],
        "strengths": ["Cooperation", "Empathy", "Patience"],
        "weaknesses": ["Indecision", "Over-sensitivity", "Avoidance"],
        "business": "Working in partnerships or mediating conflicts.",
        "relationships": "Building strong, harmonious relationships.",
        "purpose": "To foster peace and understanding through collaboration."
    },
    3: {
        "description": "Pinnacle 3 brings creativity, self-expression, and social energy. It’s a time to enjoy life and communicate openly.",
        "advice": "Express yourself freely, but be mindful not to scatter your energy.",
        "master": False,
        "traits": ["Creative", "Optimistic", "Social"],
        "strengths": ["Communication", "Joyfulness", "Imagination"],
        "weaknesses": ["Restlessness", "Superficiality", "Over-excitement"],
        "business": "Pursuing creative projects or working in communications.",
        "relationships": "Enjoying social connections and expressing your feelings.",
        "purpose": "To inspire joy and creativity through self-expression."
    },
    4: {
        "description": "Pinnacle 4 calls for discipline, hard work, and building solid foundations. It’s a time for responsibility and organization.",
        "advice": "Be patient and persistent. Avoid rigidity or resistance to change.",
        "master": False,
        "traits": ["Organized", "Reliable", "Practical"],
        "strengths": ["Discipline", "Perseverance", "Focus"],
        "weaknesses": ["Stubbornness", "Pessimism", "Inflexibility"],
        "business": "Building a stable business or excelling in a structured environment.",
        "relationships": "Committing to long-term, stable relationships.",
        "purpose": "To create lasting structures and systems through dedication."
    },
    5: {
        "description": "Pinnacle 5 encourages change, freedom, and adventure. Embrace new opportunities and be adaptable.",
        "advice": "Stay flexible and open-minded. Avoid impulsiveness or recklessness.",
        "master": False,
        "traits": ["Adventurous", "Energetic", "Curious"],
        "strengths": ["Versatility", "Resourcefulness", "Freedom-loving"],
        "weaknesses": ["Restlessness", "Impatience", "Inconsistency"],
        "business": "Adapting to new markets or exploring unconventional career paths.",
        "relationships": "Embracing change and adventure in your relationships.",
        "purpose": "To explore new horizons and inspire others to embrace freedom."
    },
    6: {
        "description": "Pinnacle 6 emphasizes love, family, and responsibility. Focus on nurturing relationships and creating harmony.",
        "advice": "Balance care for others with self-care. Avoid overprotectiveness or worry.",
        "master": False,
        "traits": ["Caring", "Responsible", "Supportive"],
        "strengths": ["Compassion", "Harmony", "Reliability"],
        "weaknesses": ["Overprotectiveness", "Martyrdom", "Anxiety"],
        "business": "Creating a supportive work environment or working in a care-related field.",
        "relationships": "Nurturing your family and creating a harmonious home life.",
        "purpose": "To create a loving and supportive environment for yourself and others."
    },
    7: {
        "description": "Pinnacle 7 is a period for introspection, study, and spiritual growth. Seek knowledge and trust your intuition.",
        "advice": "Allow time for solitude and reflection. Avoid skepticism or isolation.",
        "master": False,
        "traits": ["Analytical", "Introspective", "Spiritual"],
        "strengths": ["Wisdom", "Intuition", "Focus"],
        "weaknesses": ["Isolation", "Cynicism", "Secretiveness"],
        "business": "Working in research, writing, or a spiritually-oriented field.",
        "relationships": "Seeking deep, meaningful connections with others.",
        "purpose": "To uncover hidden truths and share your wisdom with the world."
    },
    8: {
        "description": "Pinnacle 8 focuses on power, success, and material achievement. It’s a time to work hard and lead with integrity.",
        "advice": "Aim for balanced ambition and ethical leadership. Avoid greed or workaholism.",
        "master": False,
        "traits": ["Ambitious", "Efficient", "Pragmatic"],
        "strengths": ["Leadership", "Organization", "Confidence"],
        "weaknesses": ["Domineering", "Materialism", "Stubbornness"],
        "business": "Achieving financial success and leading with integrity.",
        "relationships": "Building strong, supportive relationships with ambitious partners.",
        "purpose": "To achieve material success and use your power for good."
    },
    9: {
        "description": "Pinnacle 9 is about completion, compassion, and humanitarian efforts. It encourages letting go and embracing generosity.",
        "advice": "Practice forgiveness and service. Avoid emotional overwhelm or idealism.",
        "master": False,
        "traits": ["Compassionate", "Idealistic", "Generous"],
        "strengths": ["Tolerance", "Creativity", "Empathy"],
        "weaknesses": ["Over-sensitivity", "Naivety", "Impatience"],
        "business": "Working in a non-profit or creating a socially responsible business.",
        "relationships": "Practicing forgiveness and letting go of past hurts.",
        "purpose": "To uplift humanity and contribute to a better world."
    },
    11: {
        "description": "Master Pinnacle 11 inspires spiritual awakening, intuition, and illumination. It’s a period of high sensitivity and insight.",
        "advice": "Trust your inner guidance and use your vision to uplift others.",
        "master": True,
        "traits": ["Visionary", "Inspirational", "Sensitive"],
        "strengths": ["Intuition", "Creativity", "Empathy"],
        "weaknesses": ["Anxiety", "Emotional overwhelm", "Restlessness"],
        "business": "Using your intuition and creativity to inspire others in your career.",
        "relationships": "Connecting with others on a deep, spiritual level.",
        "purpose": "To inspire and enlighten others with your spiritual insights."
    },
    22: {
        "description": "Master Pinnacle 22 offers the ability to manifest grand visions with practicality and strength.",
        "advice": "Use your power wisely to build lasting foundations.",
        "master": True,
        "traits": ["Powerful", "Disciplined", "Visionary"],
        "strengths": ["Leadership", "Strategic planning", "Determination"],
        "weaknesses": ["Perfectionism", "Workaholism", "Control issues"],
        "business": "Building large-scale projects that benefit humanity.",
        "relationships": "Creating a strong, stable partnership to support your shared vision.",
        "purpose": "To build lasting structures and systems that benefit humanity."
    },
    33: {
        "description": "Master Pinnacle 33 focuses on spiritual teaching, compassion, and healing. It’s a time to serve others selflessly.",
        "advice": "Balance service with self-care to avoid burnout.",
        "master": True,
        "traits": ["Compassionate", "Selfless", "Inspirational"],
        "strengths": ["Healing", "Teaching", "Empathy"],
        "weaknesses": ["Self-sacrifice", "Overwhelm", "Martyrdom"],
         "business": "Using your gifts to heal and support others in your career.",
        "relationships": "Nurturing your relationships with unconditional love and compassion.",
        "purpose": "To heal and uplift humanity through selfless service and love."
    }
}

def get_pinnacle_meaning(number: int) -> dict:
    """Return pinnacle number meaning including master numbers."""
    if number not in pinnacle_meanings:
        return {
            "summary": "Invalid Pinnacle number.",
            "advice": "Please enter a valid Pinnacle number (1-9, 11, 22, 33).",
            "master": False,
            "traits": [],
            "strengths": [],
            "weaknesses": [],
            "business": None,
            "relationships": None,
            "purpose": None
        }
    meaning = pinnacle_meanings[number]
    print(f"Pinnacle Number {number}:")
    print("Description:", meaning['description'])
    print("Advice:", meaning['advice'])
    print("Traits:", ', '.join(meaning['traits']))
    print("Strengths:", ', '.join(meaning['strengths']))
    print("Weaknesses:", ', '.join(meaning['weaknesses']))
    print("Business:", meaning['business'])
    print("Relationships:", meaning['relationships'])
    print("Purpose:", meaning['purpose'])
    return meaning

def calculate_pinnacle_numbers(birth_date_str: str) -> list[int | str]:
    """Calculates all four pinnacle numbers from a birth date."""
    components = get_reduced_date_components(birth_date_str)
    if isinstance(components, str):
        return [f"Cannot calculate Pinnacles: {components}"] * 4  # Return error for all
    r_month, r_day, r_year = components
    if not all(isinstance(i, int) for i in [r_month, r_day, r_year]):
        return ["Invalid date components for Pinnacles."] * 4
    try:
        pinnacle1 = reduce_number(r_month + r_day)
        pinnacle2 = reduce_number(r_day + r_year)
        pinnacle3 = reduce_number(pinnacle1 + pinnacle2)
        pinnacle4 = reduce_number(r_month + r_year)
        return [pinnacle1, pinnacle2, pinnacle3, pinnacle4]
    except Exception as e:
        return [f"Error calculating Pinnacles: {e}"] * 4

def get_pinnacle_analysis(number: int) -> dict:
    """Return pinnacle number meaning including master numbers."""
    if number not in pinnacle_meanings:
        return {
            "summary": "Invalid Pinnacle number.",
            "advice": "Please enter a valid Pinnacle number (1-9, 11, 22, 33).",
            "master": False,
            "traits": [],
            "strengths": [],
            "weaknesses": [],
            "business": None,
            "relationships": None,
            "purpose": None
        }
    meaning = pinnacle_meanings[number]
    return {
        "summary": meaning['description'],
        "advice": meaning['advice'],
        "master": meaning['master'],
        "traits": meaning['traits'],
        "strengths": meaning['strengths'],
        "weaknesses": meaning['weaknesses'],
        "business": meaning['business'],
        "relationships": meaning['relationships'],
        "purpose": meaning['purpose'],
    }

def get_pinnacle_report_string(number: int) -> str:
    """Generates and returns a formatted string report for a given Pinnacle number."""
    analysis = get_pinnacle_analysis(number)

    report_string = "=" * 60 + "\n"
    report_string += f"🌟 Pinnacle Number {number} Report 🌟\n"
    report_string += "=" * 60 + "\n"
    report_string += f"🧾 Summary: {analysis['summary']}\n"
    report_string += f"💡 Advice: {analysis['advice']}\n"
    report_string += f"✨ Master Number: {'Yes' if analysis['master'] else 'No'}\n"
    report_string += "\n🔑 Core Traits: " + ', '.join(analysis['traits']) + "\n"
    report_string += "✅ Strengths: " + ', '.join(analysis['strengths']) + "\n"
    report_string += "⚠️ Weaknesses: " + ', '.join(analysis['weaknesses']) + "\n"
    report_string += "\n💼 Business Outlook:\n"
    report_string += f" - {analysis['business']}\n"
    report_string += "\n❤️ Relationships:\n"
    report_string += f" - {analysis['relationships']}\n"
    report_string += "\n🎯 Life Purpose:\n"
    report_string += f" - {analysis['purpose']}\n"
    report_string += "=" * 60 + "\n"

    return report_string

def generate_pinnacle_report(birth_date_str: str) -> dict:
    """Generates a report containing the pinnacle numbers and their meanings."""
    pinnacle_numbers = calculate_pinnacle_numbers(birth_date_str)
    if any(isinstance(num, str) for num in pinnacle_numbers):  # Check for errors
        return {"error": pinnacle_numbers[0]}  # Return the first error message

    report = {}
    for i in range(1, 5):
        number = pinnacle_numbers[i-1]
        if isinstance(number, str):
            report[f"pinnacle{i}"] = {"number": number, "report": number}  # Store the error message
        else:
            report[f"pinnacle{i}"] = {"number": number, "report": get_pinnacle_report_string(number)}

    return report

def print_pinnacle_report(birth_date_str: str):
    """Calculates and prints a formatted pinnacle report to the console."""
    report = generate_pinnacle_report(birth_date_str)

    print("=" * 60)
    print("Pinnacle Report")
    print("=" * 60)

    for i in range(1, 5):
        pinnacle = report[f"pinnacle{i}"]
        number = pinnacle['number']
        pinnacle_report = pinnacle['report']

        print(f"\nPinnacle {i}: {number}")
        print(pinnacle_report)

    print("=" * 60)

# Example Usage:
if __name__ == "__main__":
    birth_date = "1987-05-08"  # Replace with an actual birth date
    print_pinnacle_report(birth_date)