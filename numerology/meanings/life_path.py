# from numerology.meanings.numerology_meanings import life_path_meanings


LIFE_PATH_INTERPRETATIONS = {
    1: {
        "description": "The Leader. Ones are ambitious and self-motivated individuals with a strong drive to achieve personal success.",
        "advice": "Use your leadership wisely; avoid arrogance. Stay open to teamwork and input from others.",
        "master": False,
        "element": "Fire",
        "traits": ["Leadership", "Initiative", "Courage"],
        "strengths": ["Determined", "Confident", "Innovative"],
        "weaknesses": ["Stubborn", "Impatient", "Dominating"],
        "business": "Your pioneering spirit and leadership make you a natural entrepreneur. Focus on innovation and building your own path.",
        "purpose": "To lead by example and inspire others to pursue their goals boldly.",
        "relationships": "You value independence; seek partners who respect your need for freedom and support your ambitions."
    },
    2: {
        "description": "The Diplomat. Twos are gentle, intuitive, and cooperative, often excelling in roles that require empathy and harmony.",
        "advice": "Don’t avoid conflict at the cost of your own needs. Learn to speak up when necessary.",
        "master": False,
        "element": "Water",
        "traits": ["Harmony", "Sensitivity", "Supportiveness"],
        "strengths": ["Cooperative", "Empathetic", "Patient"],
        "weaknesses": ["Overly passive", "Indecisive", "Easily hurt"],
        "business": "You thrive in partnerships and behind-the-scenes roles. Consider mediation, counseling, or support-focused careers.",
        "purpose": "To bring peace and cooperation into the world, helping others feel understood.",
        "relationships": "You need emotional depth and loyalty. Your ideal partner values emotional intelligence and mutual respect."
    },
    3: {
        "description": "The Communicator. Threes are expressive, artistic, and social, often drawn to creative and entertaining pursuits.",
        "advice": "Balance your desire for fun with discipline. Don’t scatter your energy too widely.",
        "master": False,
        "element": "Air",
        "traits": ["Creativity", "Optimism", "Expression"],
        "strengths": ["Charming", "Artistic", "Enthusiastic"],
        "weaknesses": ["Superficial", "Moody", "Disorganized"],
        "business": "You shine in roles requiring communication and flair. Media, writing, and arts are natural fields.",
        "purpose": "To inspire others through creativity and joy, uplifting the world with your voice.",
        "relationships": "You bring lightness to relationships but need a partner who keeps you grounded and focused."
    },
    4: {
        "description": "The Builder. Fours are practical, disciplined, and grounded individuals who value order and hard work.",
        "advice": "Be open to flexibility and creativity. Don’t get trapped in routines or excessive rigidity.",
        "master": False,
        "element": "Earth",
        "traits": ["Stability", "Discipline", "Responsibility"],
        "strengths": ["Loyal", "Organized", "Reliable"],
        "weaknesses": ["Rigid", "Overly cautious", "Judgmental"],
        "business": "You excel in structured environments. Construction, engineering, or project management suit your methodical nature.",
        "purpose": "To create lasting structures—physical or metaphorical—that bring security and order.",
        "relationships": "You are loyal and committed. You need a dependable partner who shares your values and work ethic."
    },
    5: {
        "description": "The Adventurer. Fives are dynamic, curious, and freedom-loving individuals who crave variety and experience.",
        "advice": "Channel your energy constructively. Avoid recklessness and overindulgence.",
        "master": False,
        "element": "Air",
        "traits": ["Freedom", "Adaptability", "Curiosity"],
        "strengths": ["Versatile", "Energetic", "Progressive"],
        "weaknesses": ["Restless", "Irresponsible", "Impulsive"],
        "business": "You thrive in travel, media, sales, or anything that offers constant change and stimulation.",
        "purpose": "To explore life’s possibilities and show others the power of personal freedom and change.",
        "relationships": "You seek excitement and mental stimulation. A flexible and adventurous partner suits you best."
    },
    6: {
        "description": "The Nurturer. Sixes are compassionate, responsible, and family-oriented, often taking on caregiver roles.",
        "advice": "Don't lose yourself in helping others. Set healthy boundaries and practice self-care.",
        "master": False,
        "element": "Earth",
        "traits": ["Responsibility", "Service", "Compassion"],
        "strengths": ["Loving", "Protective", "Loyal"],
        "weaknesses": ["Overbearing", "Self-sacrificing", "Judgmental"],
        "business": "You do well in caregiving, education, or community service—roles that let you nurture others.",
        "purpose": "To heal and support others, building harmony through love and service.",
        "relationships": "You are devoted and protective. You seek a stable, loving partner who values family and loyalty."
    },
    7: {
        "description": "The Seeker. Sevens are introspective, analytical, and spiritual, constantly searching for deeper truths.",
        "advice": "Avoid isolation and cynicism. Stay connected to others while pursuing your inner path.",
        "master": False,
        "element": "Water",
        "traits": ["Wisdom", "Intuition", "Analysis"],
        "strengths": ["Insightful", "Reflective", "Independent"],
        "weaknesses": ["Aloof", "Overly critical", "Withdrawn"],
        "business": "You are suited for research, science, philosophy, or spirituality. Deep thinking is your asset.",
        "purpose": "To uncover hidden truths and bring spiritual or intellectual insights to the world.",
        "relationships": "You need a partner who respects your need for space and supports your inner journey."
    },
    8: {
        "description": "The Executive. Eights are ambitious, driven, and capable of great success in the material world.",
        "advice": "Use power responsibly. Balance ambition with ethics and compassion.",
        "master": False,
        "element": "Fire",
        "traits": ["Power", "Success", "Authority"],
        "strengths": ["Strategic", "Resilient", "Goal-oriented"],
        "weaknesses": ["Controlling", "Materialistic", "Workaholic"],
        "business": "You thrive in business, finance, and leadership roles. You have the drive to build empires.",
        "purpose": "To master the material world and use wealth and power to create lasting impact.",
        "relationships": "You need a strong, supportive partner who understands your goals and can handle your intensity."
    },
    9: {
        "description": "The Humanitarian. Nines are compassionate, idealistic, and generous, devoted to serving the greater good.",
        "advice": "Let go of the past and avoid martyrdom. Balance giving with receiving.",
        "master": False,
        "element": "Water",
        "traits": ["Compassion", "Idealism", "Wisdom"],
        "strengths": ["Charitable", "Visionary", "Forgiving"],
        "weaknesses": ["Overly emotional", "Self-righteous", "Escapist"],
        "business": "You’re drawn to philanthropy, arts, or global causes. Your purpose goes beyond material gain.",
        "purpose": "To uplift humanity and contribute to a better world through selfless service.",
        "relationships": "You are deep and emotional. Your ideal partner shares your vision and values empathy."
    },
    11: {
        "description": "The Visionary. Elevens are spiritually gifted, intuitive, and inspiring, often acting as channels for higher wisdom.",
        "advice": "Ground your visions in action. Don't let emotional sensitivity paralyze you.",
        "master": True,
        "element": "Air",
        "traits": ["Inspiration", "Intuition", "Spiritual Insight"],
        "strengths": ["Visionary", "Empathic", "Charismatic"],
        "weaknesses": ["Overwhelmed", "Anxious", "Unrealistic"],
        "business": "You do well in spiritual, artistic, or counseling roles that let you inspire and uplift.",
        "purpose": "To enlighten and awaken others, using your intuition and creativity as a guide.",
        "relationships": "You seek a soulful connection. Your partner should honor your emotional depth and dreams."
    },
    22: {
        "description": "The Master Builder. Twenty-twos combine dreams with practical action, capable of manifesting large-scale achievements.",
        "advice": "Avoid self-doubt. Embrace your potential and focus your vision with discipline.",
        "master": True,
        "element": "Earth",
        "traits": ["Manifestation", "Vision", "Leadership"],
        "strengths": ["Master planner", "Determined", "Balanced"],
        "weaknesses": ["Overburdened", "Detached", "Overcontrolling"],
        "business": "You excel in architecture, global enterprise, or systems-building—anything requiring big thinking and strategy.",
        "purpose": "To turn dreams into reality and leave a tangible legacy for humanity.",
        "relationships": "You need a grounded, supportive partner who helps you maintain balance and focus."
    },
    33: {
        "description": "The Master Healer. Thirty-threes are nurturing, wise, and devoted to selfless service with spiritual purpose.",
        "advice": "Don’t neglect your own needs. Learn to say no and create healthy boundaries.",
        "master": True,
        "element": "Water",
        "traits": ["Compassion", "Service", "Wisdom"],
        "strengths": ["Healing", "Devotion", "Emotional intelligence"],
        "weaknesses": ["Overwhelmed", "Self-sacrificing", "Emotionally drained"],
        "business": "You thrive in healing arts, teaching, or humanitarian work where love and wisdom are needed.",
        "purpose": "To uplift and heal others through unconditional love and spiritual service.",
        "relationships": "You seek deep soul connections. A loving, emotionally aware partner is essential to your path."
    }
}

def get_life_path_analysis(number: int, user_goals=None) -> dict:
    """
    Return a smart, detailed analysis for a given Life Path number.
    Accepts master numbers. Incorporates context like user's goals.
    """
    meaning = LIFE_PATH_INTERPRETATIONS.get(number)

    if not meaning:
        print("DEBUG: Invalid Life Path number")
        return {
            "summary": "Invalid Life Path number.",
            "insights": [],
            "actions": [],
            "recommendation": "Please enter a valid Life Path number (1-9, 11, 22, 33)."
        }

    insights = []
    print(f"DEBUG: Analyzing Life Path {number}")
    print(f"DEBUG: Meaning: {meaning}")  # Print the 'meaning' dictionary

    # Deeper insights based on traits
    if "Leadership" in meaning['traits']:
        insights.append("Lead with inspiration, not control. People naturally look to you for direction.")
        print("DEBUG: Added Leadership insight")
    if "Empathy" in meaning['traits']:
        insights.append("Use your emotional awareness to support, guide, and heal others.")
        print("DEBUG: Added Empathy insight")
    if "Creativity" in meaning['traits']:
        insights.append("You may thrive in artistic or original pursuits. Trust your creative flow.")
        print("DEBUG: Added Creativity insight")
    if "Discipline" in meaning['traits']:
        insights.append("Your structured mindset makes you a powerful builder of long-term goals.")
        print("DEBUG: Added Discipline insight")
    if "Spirituality" in meaning['traits']:
        insights.append("You have a calling toward deeper meaning. Don't ignore your inner voice.")
        print("DEBUG: Added Spirituality insight")

    # Goal-specific guidance
    if user_goals:
        user_goals_lower = user_goals.lower()
        if "find purpose" in user_goals_lower:
            print(f"DEBUG: meaning['purpose']: {meaning['purpose']}")  # Add this line
            insights.append(f"Your purpose is to {meaning['purpose'].lower()}")
            print("DEBUG: Added find purpose insight")
        print(f"DEBUG: User goals: {user_goals_lower}")
    if "business" in user_goals_lower or "entrepreneur" in user_goals_lower:
        if "Leadership" in meaning['traits'] or "Innovative" in meaning['strengths']:
                insights.append("You're naturally suited for leadership roles or starting your own venture.")
                print("DEBUG: Added business/entrepreneur insight")
    if "relationship" in user_goals_lower:
        if "Empathy" in meaning['traits'] or meaning['element'] in ["Water", "Air"]:
                insights.append("You’re emotionally attuned—seek someone who reciprocates your depth.")
                print("DEBUG: Added relationship insight")
  
          
    else:
        # Add default insights if no user goals are provided
        insights.append("Focus on your core strengths to achieve personal fulfillment.")
        insights.append("Reflect on your weaknesses and identify strategies for improvement.")
        print("DEBUG: Added default insights")

    # Smart actions
    actions = [
        "Reflect on whether you’re living up to your strengths and minimizing your weaknesses.",
        "Write a journal entry about how your element ({} – {}) influences your decision-making.".format(
            meaning['element'], ", ".join(meaning['traits'])),
        "Align one personal or professional goal with your Life Path energy this week.",
    ]

    print(f"DEBUG: Insights: {insights}")  # Print the final insights list
    return {
        "summary": f"Life Path {number} - {meaning['description']}",
        "element": meaning['element'],
        "traits": meaning['traits'],
        "strengths": meaning['strengths'],
        "weaknesses": meaning['weaknesses'],
        "advice": meaning['advice'],
        "business": meaning['business'],
        "purpose": meaning['purpose'],
        "relationships": meaning['relationships'],
        "insights": insights,
        "actions": actions
    }

def get_life_path_report_string(number, user_goals=None):
    """
    Generates and returns a formatted string report for a given Life Path number.
    """
    analysis = get_life_path_analysis(number, user_goals)

    report_string = "=" * 60 + "\n"
    report_string += f"🌟 Life Path {number} Report 🌟\n"
    report_string += "=" * 60 + "\n"
    report_string += f"🧾 Summary: {analysis['summary']}\n"
    report_string += f"🜂 Element: {analysis['element']}\n"
    report_string += "\n🔑 Core Traits: " + ', '.join(analysis['traits']) + "\n"
    report_string += "✅ Strengths: " + ', '.join(analysis['strengths']) + "\n"
    report_string += "⚠️ Weaknesses: " + ', '.join(analysis['weaknesses']) + "\n"
    report_string += "\n🧠 Insights:\n"
    for insight in analysis['insights']:
        report_string += f" - {insight}\n"
    report_string += "\n📌 Recommended Actions:\n"
    for action in analysis['actions']:
        report_string += f" - {action}\n"
    report_string += "\n💼 Business Outlook:\n"
    report_string += f" - {analysis['business']}\n"
    report_string += "\n🎯 Life Purpose:\n"
    report_string += f" - {analysis['purpose']}\n"
    report_string += "\n❤️ Relationships:\n"
    report_string += f" - {analysis['relationships']}\n"
    report_string += "\n💡 Advice:\n"
    report_string += f" - {analysis['advice']}\n"
    report_string += "=" * 60 + "\n"

    return report_string

