

import sys
sys.path.append('/media/jeff/numy/numerology_ai')


karmic_lessons_meanings = {
    1: {
        "description": "You may struggle with asserting yourself or fear being independent. Lesson is to develop courage and leadership.",
        "advice": "Work on self-confidence and taking initiative without fear of rejection.",
        "master": False,
        "traits": ["Dependent", "Passive", "Shy"],
        "strengths": ["Courage", "Independence", "Leadership"],
        "weaknesses": ["Fearful", "Avoids conflict", "Low self-esteem"],
        "business": "Starting a business where you are the leader, taking on leadership roles.",
        "relationships": "Learning to be independent and assertive in relationships.",
        "purpose": "To develop unwavering self-belief and inspire others to do the same.",
        "color": "Red",
        "vibration": "Initiating, Focused, Dynamic"
    },
    2: {
        "description": "Lessons around cooperation, patience, and sensitivity. You might avoid confrontation or overcompromise.",
        "advice": "Learn to assert your needs gently and build healthy partnerships.",
        "master": False,
        "traits": ["Overly sensitive", "Indecisive", "Avoids conflict"],
        "strengths": ["Diplomatic", "Patient", "Cooperative"],
        "weaknesses": ["Passive", "People-pleasing", "Fear of rejection"],
        "business": "Working in partnerships, mediation, or customer service roles.",
        "relationships": "Finding a balance between your needs and the needs of your partner.",
        "purpose": "To foster harmony and understanding in all your interactions.",
        "color": "Orange",
        "vibration": "Receptive, Harmonious, Intuitive"
    },
    3: {
        "description": "You may hold back your creative self-expression due to fear of judgment or lack of confidence.",
        "advice": "Practice joyful expression and embrace your creativity without fear.",
        "master": False,
        "traits": ["Inhibited", "Self-critical", "Quiet"],
        "strengths": ["Creative", "Expressive", "Optimistic"],
        "weaknesses": ["Shy", "Self-doubting", "Reserved"],
        "business": "Expressing your creativity in a business setting, marketing, or the arts.",
        "relationships": "Expressing your feelings and ideas openly in relationships.",
        "purpose": "To inspire joy and creativity in the world through your unique self-expression.",
        "color": "Yellow",
        "vibration": "Joyful, Expressive, Uplifting"
    },
    4: {
        "description": "Lessons about discipline, patience, and responsibility. You may struggle with laziness or inconsistency.",
        "advice": "Develop focus, hard work habits, and build solid foundations.",
        "master": False,
        "traits": ["Unfocused", "Irresponsible", "Impatient"],
        "strengths": ["Organized", "Reliable", "Diligent"],
        "weaknesses": ["Procrastination", "Restlessness", "Avoidance"],
        "business": "Building a stable and organized business, excelling in structured environments.",
        "relationships": "Committing to long-term, stable relationships.",
        "purpose": "To create lasting structures and systems that bring stability and order to the world.",
        "color": "Green",
        "vibration": "Grounded, Practical, Stable"
    },
    5: {
        "description": "You might have difficulties with commitment or fear of freedom loss. Lessons to balance change with stability.",
        "advice": "Embrace change but learn responsibility and consistency.",
        "master": False,
        "traits": ["Fearful of commitment", "Restless", "Inconsistent"],
        "strengths": ["Adaptable", "Adventurous", "Curious"],
        "weaknesses": ["Impulsive", "Unreliable", "Impatient"],
        "business": "Adapting to change in a business environment, taking risks, and being versatile.",
        "relationships": "Balancing the need for freedom with the responsibilities of a relationship.",
        "purpose": "To explore the world and inspire others to embrace change and freedom.",
        "color": "Blue",
        "vibration": "Free-spirited, Curious, Transformative"
    },
    6: {
        "description": "Lessons focus on responsibility, care, and balance between self and others. May struggle with neglect or overprotection.",
        "advice": "Learn to nurture without losing your own identity.",
        "master": False,
        "traits": ["Neglectful", "Overbearing", "Worrier"],
        "strengths": ["Caring", "Loving", "Supportive"],
        "weaknesses": ["Martyrdom", "Overprotectiveness", "Anxiety"],
        "business": "Creating a caring and supportive business environment, working in care-related industries.",
        "relationships": "Balancing the needs of others with your own needs in relationships.",
        "purpose": "To heal and support others, creating harmony and balance in your community.",
        "color": "Indigo",
        "vibration": "Nurturing, Responsible, Harmonizing"
    },
    7: {
        "description": "You may struggle with trust, isolation, or skepticism. Lessons involve opening up and seeking deeper knowledge.",
        "advice": "Balance solitude with social connection and faith.",
        "master": False,
        "traits": ["Isolated", "Skeptical", "Cynical"],
        "strengths": ["Introspective", "Analytical", "Wise"],
        "weaknesses": ["Lonely", "Distrustful", "Withdrawn"],
        "business": "Using your analytical skills in research, science, or spiritual pursuits.",
        "relationships": "Building trust and intimacy in relationships.",
        "purpose": "To uncover hidden truths and bring spiritual or intellectual insights to the world.",
        "color": "Violet",
        "vibration": "Mystical, Insightful, Deep"
    },
    8: {
        "description": "Lessons in power, control, and material success. You might abuse power or fear failure.",
        "advice": "Lead with integrity and balance material goals with ethics.",
        "master": False,
        "traits": ["Controlling", "Fearful of failure", "Domineering"],
        "strengths": ["Ambitious", "Organized", "Determined"],
        "weaknesses": ["Greedy", "Manipulative", "Impatient"],
        "business": "Using power and resources responsibly in business, leading with integrity.",
        "relationships": "Sharing power and control equally in relationships.",
        "purpose": "To achieve material success and use your power for good.",
        "color": "Black",
        "vibration": "Powerful, Authoritative, Magnetic"
    },
    9: {
        "description": "Lessons involve compassion, letting go, and humanitarianism. You may hold onto pain or avoid endings.",
        "advice": "Practice forgiveness and embrace closure for growth.",
        "master": False,
        "traits": ["Resentful", "Clinging", "Overly emotional"],
        "strengths": ["Compassionate", "Generous", "Visionary"],
        "weaknesses": ["Self-pity", "Naivety", "Impatience"],
        "business": "Creating a business that aligns with humanitarian values, working in non-profits.",
        "relationships": "Practicing forgiveness and letting go of past hurts in relationships.",
        "purpose": "To uplift humanity and contribute to a better world through selfless service and compassion.",
        "color": "White",
        "vibration": "Compassionate, Global, Transformational"
    },
    11: {
        "description": "Master number 11 transcends karmic lessons but may face challenges in balancing intuition and practicality.",
        "advice": "Focus on spiritual growth while staying grounded.",
        "master": True,
        "traits": ["Intuitive", "Visionary", "Sensitive"],
        "strengths": ["Inspiration", "Spiritual insight", "Leadership"],
        "weaknesses": ["Anxiety", "Tension", "Overwhelm"],
        "business": "Using intuition and spiritual insight in a business or creative venture.",
        "relationships": "Connecting with others on a deep, spiritual level.",
        "purpose": "To inspire and enlighten others with your spiritual insights.",
        "color": "Silver",
        "vibration": "Illuminating, Psychic, Enlightening"
    },
    22: {
        "description": "Master number 22 focuses on building and manifesting visions. Karmic lessons are about responsibility at high levels.",
        "advice": "Balance ambition with humility and service.",
        "master": True,
        "traits": ["Practical", "Powerful", "Disciplined"],
        "strengths": ["Leadership", "Vision", "Determination"],
        "weaknesses": ["Perfectionism", "Workaholism", "Stubbornness"],
        "business": "Building large-scale projects that benefit humanity, leading with responsibility.",
        "relationships": "Creating a strong and stable partnership to support your shared vision.",
        "purpose": "To manifest your dreams into reality and create lasting structures that benefit humanity.",
        "color": "Gold",
        "vibration": "Master Builder, Global Impact, Infinite Potential"
    },
    33: {
        "description": "Master number 33 is the master teacher with high spiritual calling. Lessons revolve around selfless service.",
        "advice": "Serve others while maintaining self-care.",
        "master": True,
        "traits": ["Compassionate", "Selfless", "Inspirational"],
        "strengths": ["Healing", "Teaching", "Empathy"],
        "weaknesses": ["Self-sacrifice", "Overwhelmed", "Martyrdom"],
        "business": "Creating a business that provides healing and support, teaching, or spiritual guidance.",
        "relationships": "Nurturing relationships with unconditional love and compassion.",
        "purpose": "To heal and uplift humanity through selfless service and unconditional love.",
        "color": "Rose Pink",
        "vibration": "Master Healer, Unconditional Love, Divine Service"
    }
}
def get_karmic_lesson_analysis(karmic_lessons):
    """
    Given a list of karmic lesson numbers, returns a detailed multi-line string
    describing each lesson with description, advice, traits, and more.
    """
    if not karmic_lessons:
        return "No karmic lessons found."

    analysis_lines = []
    for lesson in sorted(set(karmic_lessons)):
        lesson_data = karmic_lessons_meanings.get(lesson)
        if not lesson_data:
            analysis_lines.append(f"Lesson {lesson}: Meaning not found.")
            continue
        
        lines = [
            f"Lesson {lesson}:",
            f"  Description: {lesson_data.get('description', 'N/A')}",
            f"  Advice: {lesson_data.get('advice', 'N/A')}",
            f"  Traits: {', '.join(lesson_data.get('traits', []))}",
            f"  Strengths: {', '.join(lesson_data.get('strengths', []))}",
            f"  Weaknesses: {', '.join(lesson_data.get('weaknesses', []))}",
            f"  Business: {lesson_data.get('business', 'N/A')}",
            f"  Relationships: {lesson_data.get('relationships', 'N/A')}",
            f"  Purpose: {lesson_data.get('purpose', 'N/A')}",
            f"  Color: {lesson_data.get('color', 'N/A')}",
            f"  Vibration: {lesson_data.get('vibration', 'N/A')}",
            ""
        ]
        analysis_lines.extend(lines)

    return "\n".join(analysis_lines)
if __name__ == "__main__":
    test_lessons = [1, 2]
    print(get_karmic_lesson_analysis(test_lessons))
