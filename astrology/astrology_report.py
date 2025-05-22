# /media/jeff/numy/numerology_ai/astrology/astrology_report.py
import swisseph as swe
import datetime
import os

try:
    from .sign_meanings import sign_definitions as imported_sign_meanings
    from .planet_meanings import planet_definitions as imported_planet_meanings
    from .aspect_meanings import get_aspect_analysis, get_aspect_report_string
    from .moon_sign_meaning import get_moon_in_sign_details
    from .element_meanings import element_definitions as imported_element_definitions
    from .modality_meanings import modality_definitions as imported_modality_definitions
except ImportError:
    print(
        "Warning from astrology_report: Could not import one or more meaning definitions from .astrology_data.*"
    )
    imported_sign_meanings, imported_planet_meanings = {}, {}
    imported_element_definitions, imported_modality_definitions = {}, {}
    def get_aspect_analysis(aspect_name: str) -> dict: return {"error": f"Aspect analysis unavailable for {aspect_name}"}
    def get_aspect_report_string(aspect_name: str) -> str: return f"Aspect report unavailable for {aspect_name}"
    def get_moon_in_sign_details(moon_sign: str) -> dict: return {"summary": "Moon sign details unavailable."}

try:
    from .zodiac import (
        degree_to_sign,
        PLANET_NAMES, # This might be defined locally if not from zodiac
        # get_sun_sign, get_moon_sign, get_sign_details, element, modality,
        # calculate_aspects_within_chart, ASPECT_ANGLES, ASPECT_TYPES # These might not be directly used here if chart_data provides all
    )
except ImportError as e:
    print(f"Warning from astrology_report: Could not import from .zodiac: {e}")
    def degree_to_sign(lon): return "Unknown Sign (Longitude Error)"
    PLANET_NAMES = {}


try:
    from astrology.birth_chart import generate_birth_chart
    # get_planet_positions might not be directly called if generate_birth_chart returns it
except ImportError as e:
    print(f"Warning from astrology_report: Could not import from astrology.birth_chart: {e}")
    def generate_birth_chart(*args, **kwargs): return {"error": "Birth chart generation unavailable"}

try:
    from .astro_meanings import get_house_report_string, get_house_info
except ImportError as e:
    print(f"Warning from astrology_report: Could not import from .astro_meanings: {e}")
    def get_house_report_string(house_number: int) -> str: return f"Error: House {house_number} report unavailable"
    def get_house_info(house_number: int) -> dict: return {"name": f"House {house_number}", "theme": "N/A", "meaning": "House info unavailable", "planet_interpretations": {}}


def format_longitude(lon: float) -> str:
    """Formats longitude into degrees, sign, minutes, seconds."""
    sign_name = degree_to_sign(lon)
    deg_in_sign = lon % 30
    degrees = int(deg_in_sign)
    minutes_full = (deg_in_sign - degrees) * 60
    minutes = int(minutes_full)
    seconds = int((minutes_full - minutes) * 60)
    return f"{degrees:02}° {sign_name} {minutes:02}'{seconds:02}\""

PLANET_LIST_FOR_REPORT = {
    "Sun": swe.SUN, "Moon": swe.MOON, "Mercury": swe.MERCURY, "Venus": swe.VENUS,
    "Mars": swe.MARS, "Jupiter": swe.JUPITER, "Saturn": swe.SATURN,
    "Uranus": swe.URANUS, "Neptune": swe.NEPTUNE, "Pluto": swe.PLUTO,
    "Chiron": swe.CHIRON, "TrueNode": swe.TRUE_NODE,
}

def format_planet_in_sign_in_house(planet_name: str, sign_name: str, house_num: int, chart_data: dict) -> str:
    """ Formats a synthesized interpretation for a planet in a sign and house. """
    planet_info = imported_planet_meanings.get(planet_name, {})
    planet_role = planet_info.get('role', f"The energy of {planet_name}")
    planet_keywords_list = planet_info.get('keywords', [])
    planet_keywords = ", ".join(planet_keywords_list)

    sign_info = imported_sign_meanings.get(sign_name, {})
    sign_summary = sign_info.get('summary', f"the characteristics of {sign_name}")
    sign_keywords_list = sign_info.get('keywords', [])
    sign_keywords = ", ".join(sign_keywords_list)

    house_details = get_house_info(house_num) if house_num else {"name": "an unknown area", "theme": "N/A", "planet_interpretations":{}}
    house_theme = house_details.get('theme', 'a specific life area')
    planet_in_house_interp = house_details.get("planet_interpretations", {}).get(planet_name, f"This placement influences your approach to {house_theme}.")

    interpretation = f"\n  --- {planet_name} in {sign_name} (House {house_num if house_num else 'N/A'}) ---\n"
    interpretation += f"     - Core {planet_name} Energy (Keywords: {planet_keywords}): {planet_role}\n"
    interpretation += f"     - Expressed through {sign_name} (Keywords: {sign_keywords}): This colors the planet's energy with {sign_summary.lower()}\n"
    interpretation += f"     - Manifesting in House {house_num if house_num else 'N/A'} (Theme: {house_theme}): {planet_in_house_interp}\n"
    synthesis_qualities = sign_keywords_list[0].lower() if sign_keywords_list else 'unique'
    interpretation += (f"     - Synthesis: When the '{planet_role.lower()}' of {planet_name} is expressed through the lens of {sign_name}, "
                       f"it takes on its {synthesis_qualities} qualities. Placed in your {house_details.get('name', f'House {house_num}')} "
                       f"(which governs '{house_theme}'), this specific combination suggests: "
                       f"{planet_in_house_interp.replace('You ', 'This means you ').replace('Your ', 'This colors your ')}\n")
    return interpretation

def calculate_element_modality_balance(planet_positions: dict, ascendant_longitude: float) -> dict:
    """Calculates the distribution of planets (+ Ascendant) across elements and modalities."""
    balance = {
        "elements": {"Fire": 0, "Earth": 0, "Air": 0, "Water": 0, "Unknown": 0},
        "modalities": {"Cardinal": 0, "Fixed": 0, "Mutable": 0, "Unknown": 0}
    }
    planets_for_balance = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

    for planet_name in planets_for_balance:
        lon = planet_positions.get(planet_name)
        if isinstance(lon, float):
            sign = degree_to_sign(lon)
            if sign != "Unknown Sign (Longitude Error)":
                sign_info = imported_sign_meanings.get(sign, {})
                el = sign_info.get("element", "Unknown")
                mod = sign_info.get("modality", "Unknown")
                balance["elements"][el] = balance["elements"].get(el, 0) + 1
                balance["modalities"][mod] = balance["modalities"].get(mod, 0) + 1
            else:
                balance["elements"]["Unknown"] += 1
                balance["modalities"]["Unknown"] += 1

    if isinstance(ascendant_longitude, float):
        asc_sign = degree_to_sign(ascendant_longitude)
        if asc_sign != "Unknown Sign (Longitude Error)":
            sign_info = imported_sign_meanings.get(asc_sign, {})
            el = sign_info.get("element", "Unknown")
            mod = sign_info.get("modality", "Unknown")
            balance["elements"][el] = balance["elements"].get(el, 0) + 1
            balance["modalities"][mod] = balance["modalities"].get(mod, 0) + 1
        else:
            balance["elements"]["Unknown"] += 1
            balance["modalities"]["Unknown"] += 1
    return balance

def format_element_modality_balance_report(balance: dict) -> str:
    """Formats the element and modality balance into a readable string with interpretations."""
    report = "\n--- Elemental & Modality Balance ---\n"
    report += "This reflects the primary energies and operational styles in your chart.\n"
    report += "Elements:\n"
    for el, count in balance["elements"].items():
        if el != "Unknown" and el in imported_element_definitions: # Check if el is a valid key
            report += f"  - {el}: {count}\n"
            el_details = imported_element_definitions.get(el, {})
            if count > 3:
                report += f"    * With a strong emphasis in {el}, {el_details.get('keywords', ['its'])[0].lower()} qualities are prominent.\n"
            elif count == 0:
                 report += f"    * A lack of {el} suggests you might consciously cultivate its traits: {el_details.get('description', '')[:100]}...\n"
    report += "Modalities:\n"
    for mod, count in balance["modalities"].items():
        if mod != "Unknown" and mod in imported_modality_definitions: # Check if mod is a valid key
            report += f"  - {mod}: {count}\n"
            mod_details = imported_modality_definitions.get(mod, {})
            if count > 3:
                 report += f"    * A strong {mod} presence indicates {mod_details.get('keywords', ['a tendency towards its style'])[0].lower()}.\n"
    return report + "\n"

def format_chart_ruler_interpretation(asc_sign: str, chart_data: dict) -> str:
    """Formats the interpretation for the Chart Ruler."""
    report = "\n--- ✨ Your Chart Ruler: Guiding Your Path ✨ ---\n"
    asc_sign_details = imported_sign_meanings.get(asc_sign, {})
    ruler_planet_name = asc_sign_details.get("ruler")

    if not ruler_planet_name:
        report += f"Could not determine the ruling planet for your Ascendant sign ({asc_sign}).\n"
        return report

    planet_positions = chart_data.get("planet_positions", {})
    planet_houses = chart_data.get("planet_houses", {})
    ruler_lon = planet_positions.get(ruler_planet_name)
    ruler_house_num = planet_houses.get(ruler_planet_name)

    if ruler_lon is None or ruler_house_num is None:
        report += f"Could not find the position (sign/house) for your Chart Ruler, {ruler_planet_name}.\n"
        return report

    ruler_sign = degree_to_sign(ruler_lon)
    report += (f"Your Ascendant is {asc_sign}, which is ruled by {ruler_planet_name}. "
               f"Therefore, {ruler_planet_name} is your Chart Ruler. This planet and its placement "
               f"significantly color your approach to life, your primary motivations, and the "
               f"areas where you direct your core energy.\n")
    report += format_planet_in_sign_in_house(ruler_planet_name, ruler_sign, ruler_house_num, chart_data)
    return report

def format_insightful_aspect_interpretation(aspect_info: dict, chart_data: dict) -> str:
    """
    Generates a more insightful interpretation of an aspect by considering
    the planets involved, their signs, and the houses they are in.
    """
    planet1_name = aspect_info.get("planet1")
    planet2_name = aspect_info.get("planet2")
    aspect_type = aspect_info.get("aspect_type")
    orb = aspect_info.get("orb")

    if not all([planet1_name, planet2_name, aspect_type, orb is not None]):
        return "  - Incomplete aspect data for detailed interpretation.\n"

    planet_positions = chart_data.get("planet_positions", {})
    planet_houses = chart_data.get("planet_houses", {})
    house1_num = planet_houses.get(planet1_name)
    house2_num = planet_houses.get(planet2_name)

    planet1_general_info = imported_planet_meanings.get(planet1_name, {})
    planet2_general_info = imported_planet_meanings.get(planet2_name, {})
    planet1_role = planet1_general_info.get('role', planet1_name)
    planet2_role = planet2_general_info.get('role', planet2_name)

    planet1_lon = planet_positions.get(planet1_name)
    planet2_lon = planet_positions.get(planet2_name)
    planet1_sign = degree_to_sign(planet1_lon) if isinstance(planet1_lon, float) else "Unknown Sign"
    planet2_sign = degree_to_sign(planet2_lon) if isinstance(planet2_lon, float) else "Unknown Sign"

    planet1_sign_info = imported_sign_meanings.get(planet1_sign, {})
    planet2_sign_info = imported_sign_meanings.get(planet2_sign, {})
    planet1_sign_style = planet1_sign_info.get('summary', f"the style of {planet1_sign}").lower()
    planet2_sign_style = planet2_sign_info.get('summary', f"the style of {planet2_sign}").lower()

    house1_details = get_house_info(house1_num) if house1_num else {"name": "Unknown House", "theme": "N/A", "planet_interpretations": {}}
    house2_details = get_house_info(house2_num) if house2_num else {"name": "Unknown House", "theme": "N/A", "planet_interpretations": {}}
    planet1_in_house1_interp = house1_details.get("planet_interpretations", {}).get(planet1_name, f"The energy of {planet1_name} influences your {house1_details.get('theme', 'life area')}.")
    planet2_in_house2_interp = house2_details.get("planet_interpretations", {}).get(planet2_name, f"The energy of {planet2_name} influences your {house2_details.get('theme', 'life area')}.")

    aspect_data = get_aspect_analysis(aspect_type)
    aspect_general_meaning = aspect_data.get('meaning', 'N/A')
    aspect_keywords = aspect_data.get('keywords', [])
    aspect_spiritual_lesson = aspect_data.get('spiritual_lesson', 'N/A')

    insight = (f"\n  * Your {planet1_name} in {planet1_sign} (House {house1_num}, themed '{house1_details.get('theme')}') "
               f"forms a {aspect_type} with your {planet2_name} in {planet2_sign} (House {house2_num}, themed '{house2_details.get('theme')}'), "
               f"with an orb of {orb:.1f}°.\n")
    insight += (f"    - This suggests a dynamic where your '{planet1_role}' (expressing itself with {planet1_sign_style}, "
                f"and manifesting in your life as: {planet1_in_house1_interp}) interacts with your '{planet2_role}' "
                f"(expressing itself with {planet2_sign_style}, and manifesting as: {planet2_in_house2_interp}).\n")
    insight += f"    - The {aspect_type} itself generally signifies: {aspect_general_meaning}\n"
    if aspect_keywords:
        insight += f"    - Keywords for this interaction include: {', '.join(aspect_keywords)}.\n"
    insight += f"    - The spiritual lesson here often involves: {aspect_spiritual_lesson}\n"
    return insight

def generate_astrology_report(
    year: int, month: int, day: int, hour: int, minute: int,
    lon: float, lat: float, ut_offset: float = 0.0, alt: float = 0,
):
    """Generates a textual astrology report based on birth data."""
    chart_data = generate_birth_chart(year, month, day, hour, minute, ut_offset, lat, lon, alt)

    if "error" in chart_data:
        return f"Error generating birth chart for astrology report: {chart_data['error']}"

    report_string = "===== Natal Astrology Report =====\n"
    report_string += f"Birth Date (Local): {year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}\n"
    report_string += f"Birth Location: Lat {lat:.2f}, Lon {lon:.2f}\n"
    if "birth_datetime_utc" in chart_data:
        report_string += f"Birth Date (UTC): {chart_data['birth_datetime_utc']}\n"
    report_string += "==================================\n\n"

    report_string += "--- Core Identity: Sun, Moon, Ascendant ---\n"
    sun_longitude = chart_data.get("planet_positions", {}).get("Sun")
    if isinstance(sun_longitude, float):
        sun_sign = degree_to_sign(sun_longitude)
        report_string += f"☀️ Your Sun Sign: {sun_sign} ({format_longitude(sun_longitude)}) ☀️\n"
        sign_details = imported_sign_meanings.get(sun_sign, {})
        report_string += f"   - Core Essence: {sign_details.get('summary', 'N/A')}\n"
        report_string += f"   - Element: {sign_details.get('element', 'N/A')}, Modality: {sign_details.get('modality', 'N/A')}, Ruler: {sign_details.get('ruler', 'N/A')}\n"
        report_string += f"   - Keywords: {', '.join(sign_details.get('keywords', []))}\n"
        report_string += f"   - Strengths: {', '.join(sign_details.get('strengths', []))}\n"
        report_string += f"   - Potential Challenges: {', '.join(sign_details.get('weaknesses', []))}\n\n"
    else:
        report_string += f"☀️ Sun: Position Error or N/A\n\n"

    moon_longitude = chart_data.get("planet_positions", {}).get("Moon")
    natal_moon_sign = degree_to_sign(moon_longitude) if isinstance(moon_longitude, float) else chart_data.get("moon_sign", "N/A")
    if isinstance(moon_longitude, float) and natal_moon_sign != "Unknown Sign (Longitude Error)" and natal_moon_sign != "Unknown":
        report_string += f"🌙 Your Moon Sign: {natal_moon_sign} ({format_longitude(moon_longitude)}) 🌙\n"
        moon_sign_interp_details = get_moon_in_sign_details(natal_moon_sign)
        report_string += f"   - Emotional Nature: {moon_sign_interp_details.get('summary', 'N/A')}\n"
        report_string += f"   - You Need: {', '.join(moon_sign_interp_details.get('needs', []))}\n"
        report_string += f"   - Your Emotional Style: {moon_sign_interp_details.get('emotional_style', 'N/A')}\n"
        sign_details_moon = imported_sign_meanings.get(natal_moon_sign, {})
        report_string += f"   - Element: {sign_details_moon.get('element', 'N/A')}, Modality: {sign_details_moon.get('modality', 'N/A')}\n\n"
    else:
        report_string += f"🌙 Moon: Position Error or {natal_moon_sign}\n\n"

    asc_longitude = chart_data.get("ascendant_longitude")
    asc_sign = "Unknown"
    if isinstance(asc_longitude, float):
        asc_sign = degree_to_sign(asc_longitude)
        report_string += f"🌅 Your Ascendant (Rising Sign): {asc_sign} ({format_longitude(asc_longitude)}) 🌅\n"
        sign_details_asc = imported_sign_meanings.get(asc_sign, {})
        report_string += f"   - Outward Persona & First Impressions: {sign_details_asc.get('summary', 'N/A')}\n"
        report_string += f"   - Element: {sign_details_asc.get('element', 'N/A')}, Modality: {sign_details_asc.get('modality', 'N/A')}\n"
        report_string += f"   - Keywords: {', '.join(sign_details_asc.get('keywords', []))}\n"
        first_house_details = get_house_info(1)
        report_string += f"   - As the Cusp of the 1st House (Self, Identity): Your approach to new beginnings and how you project yourself is strongly colored by the traits of {asc_sign}. {first_house_details.get('meaning', '')}\n\n"
    else:
        report_string += f"🌅 Ascendant: Calculation Error or N/A\n\n"

    if asc_sign != "Unknown" and asc_sign != "Unknown Sign (Longitude Error)":
         report_string += format_chart_ruler_interpretation(asc_sign, chart_data)

    balance_data = calculate_element_modality_balance(
        chart_data.get("planet_positions", {}),
        chart_data.get("ascendant_longitude")
    )
    report_string += format_element_modality_balance_report(balance_data)

    report_string += "\n--- Planetary Placements: Influences in Life Areas ---\n"
    planet_positions_data = chart_data.get("planet_positions", {})
    planet_houses = chart_data.get("planet_houses", {})
    for planet_name, _ in PLANET_LIST_FOR_REPORT.items():
        lon_val = planet_positions_data.get(planet_name)
        house_num = planet_houses.get(planet_name)
        if isinstance(lon_val, float):
            sign = degree_to_sign(lon_val)
            report_string += format_planet_in_sign_in_house(planet_name, sign, house_num, chart_data)
        else:
            report_string += f"\n  --- {planet_name}: Position Error or N/A ---\n"
    report_string += "\n"

    report_string += "\n--- Insightful Aspect Analysis (Planets in Houses) ---\n"
    aspects_list = chart_data.get("aspects", [])
    if isinstance(aspects_list, list) and aspects_list:
        if (isinstance(aspects_list[0], dict) and "info" in aspects_list[0] and "Placeholder" in aspects_list[0]["info"]):
            report_string += f"  {aspects_list[0]['info']}\n"
        else:
            limited_aspects = aspects_list[:7] # Show up to 7 detailed aspects
            if not limited_aspects:
                report_string += "  No significant aspects to detail with house insights.\n"
            for aspect_info in limited_aspects:
                if isinstance(aspect_info, dict):
                    report_string += format_insightful_aspect_interpretation(aspect_info, chart_data)
                else:
                    report_string += f"  - Could not interpret aspect data: {aspect_info}\n"
    elif isinstance(aspects_list, dict) and "info" in aspects_list:
        report_string += f"  {aspects_list['info']}\n"
    else:
        report_string += "  No significant aspects listed or error in calculation.\n"

    report_string += "\n\n--- Detailed House Meanings & Themes ---\n"
    for i in range(1, 13):
        report_string += get_house_report_string(i) + "\n"

    report_string += "\n--- End of Astrology Report ---\n"
    return report_string

if __name__ == "__main__":
    ephe_path_set = False
    try:
        eph_path = os.environ.get('SWEP_PATH', '/media/jeff/numy/numerology_ai/mp/') # Adjust to your ephemeris path
        if os.path.isdir(eph_path):
            swe.set_ephe_path(eph_path)
            print(f"Swiss Ephemeris path set to: {eph_path}")
            ephe_path_set = True
        else:
            print(f"WARNING (astrology_report.py): Swiss Ephemeris directory not found at '{eph_path}'.")
    except Exception as e_eph:
        print(f"Error setting ephemeris path in astrology_report.py: {e_eph}")

    if ephe_path_set:
        print("\n--- Generating Sample Astrology Report ---")
        report = generate_astrology_report(
            year=1990, month=3, day=15, hour=14, minute=30,
            lon=-74.0060, lat=40.7128, ut_offset=-5.0 # New York example
        )
        print(report)

        # Example 2: London
        # report_london = generate_astrology_report(
        #     year=1985, month=7, day=22, hour=9, minute=15,
        #     lon=-0.1278, lat=51.5074, ut_offset=0.0 # London example (assuming GMT, adjust if BST)
        # )
        # print("\n--- London Sample Report ---")
        # print(report_london)
    else:
        print("Skipping astrology report generation as ephemeris path is not set or other import errors occurred.")
