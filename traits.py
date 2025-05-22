# /media/jeff/numy/numerology_ai/astrology/astrology_report.py
import swisseph as swe
import datetime
import os  # Added for ephe_path setting in __main__ if not already there

try:
    # Assuming your meaning files are in a sub-package named 'astrology_data'
    from .sign_meanings import sign_definitions as imported_sign_meanings
    from .planet_meanings import planet_meanings as imported_planet_meanings
    from .house_meanings import house_meanings

    from .aspect_meanings import aspect_definitions as imported_aspect_meanings, get_aspect_report
except ImportError:
    print(
        "Warning from astrology_report: Could not import one or more meaning definitions from .astrology_data.*"
    )
    imported_sign_meanings, imported_planet_meanings, imported_aspect_meanings = (
        {},
        {},
        {},
    )
    house_meanings = {}
    def get_aspect_report(aspect_name: str) -> str:
        return f"Aspect report unavailable for {aspect_name}"


# Import from zodiac.py
try:
    from .zodiac import (
        get_sun_sign,
        get_moon_sign,
        get_sign_details,
        degree_to_sign,  # Correct function name
        element,
        modality,
        calculate_aspects_within_chart,  # If this is in zodiac.py
        PLANET_NAMES,  # If this is in zodiac.py
        ASPECT_ANGLES,  # If this is in zodiac.py
        ASPECT_TYPES,  # If this is in zodiac.py
    )
except ImportError as e:
    print(f"Warning from astrology_report: Could not import from .zodiac: {e}")

    def get_sun_sign(m, d):
        return "Unknown"

    def get_moon_sign(y, m, d, h, mi, lat, lon, alt=0):
        return "Unknown"

    def degree_to_sign(lon):
        return "Unknown"  # Fallback for degree_to_sign

    # Define fallbacks for other potentially missing functions/variables from zodiac
    element = lambda x: "Unknown"
    modality = lambda x: "Unknown"
    calculate_aspects_within_chart = lambda x, y: []
    PLANET_NAMES, ASPECT_ANGLES, ASPECT_TYPES = {}, {}, {}

# Import from calculations
try:
    from astrology.calculations.birth_chart import (
        generate_birth_chart,
        get_planet_positions,
    )  # CORRECTED IMPORT PATH FOR get_planet_positions:

except ImportError as e:
    print(f"Warning from astrology_report: Could not import from .calculations: {e}")

    def generate_birth_chart(*args, **kwargs):
        return {"error": "Birth chart generation unavailable"}

    def get_planet_positions(*args, **kwargs):
        return {"error": "Planet positions unavailable"}

# Import from astro_meanings
try:
    from .astro_meanings import get_house_report_string
except ImportError as e:
    print(f"Warning from astrology_report: Could not import from astro_meanings: {e}")

    def get_house_report_string(house_number: int) -> str:
        return f"Error: House {house_number} report unavailable"


def format_longitude(lon: float) -> str:
    """Formats longitude into degrees, sign, minutes, seconds."""
    # This function relies on degree_to_sign from .zodiac
    sign_name = degree_to_sign(lon)
    deg_in_sign = lon % 30
    degrees = int(deg_in_sign)
    minutes_full = (deg_in_sign - degrees) * 60
    minutes = int(minutes_full)
    seconds = int((minutes_full - minutes) * 60)
    return f"{degrees:02}° {sign_name} {minutes:02}'{seconds:02}\""


# Define PLANET_LIST here if it's used in this module and not imported
# This should match the PLANET_LIST in astrology/calculations/planets.py if it's the same list
PLANET_LIST_FOR_REPORT = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mercury": swe.MERCURY,
    "Venus": swe.VENUS,
    "Mars": swe.MARS,
    "Jupiter": swe.JUPITER,
    "Saturn": swe.SATURN,
    "Uranus": swe.URANUS,
    "Neptune": swe.NEPTUNE,
    "Pluto": swe.PLUTO,
    "Chiron": swe.CHIRON,
    "TrueNode": swe.TRUE_NODE,
}


def generate_astrology_report(
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int,
    lon: float,
    lat: float,
    ut_offset: float = 0.0,
    alt: float = 0,
):
    """Generates a textual astrology report based on birth data."""
    chart_data = generate_birth_chart(
        year, month, day, hour, minute, ut_offset, lat, lon, alt
    )

    if "error" in chart_data:
        return f"Error generating birth chart for astrology report: {chart_data['error']}"

    report_string = "===== Natal Astrology Report =====\n"
    report_string += (
        f"Birth Date (Local): {year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}\n"
    )
    report_string += f"Birth Location: Lat {lat:.2f}, Lon {lon:.2f}\n"
    if "birth_datetime_utc" in chart_data:
        report_string += f"Birth Date (UTC): {chart_data['birth_datetime_utc']}\n"
    report_string += "----------------------------------\n\n"

    sun_longitude = chart_data.get("planet_positions", {}).get("Sun", "N/A")
    if isinstance(sun_longitude, float):
        sun_sign = degree_to_sign(sun_longitude)
        report_string += f"☉ Sun: {format_longitude(sun_longitude)} ({sun_sign})\n"
        sign_def = imported_sign_meanings.get(sun_sign, {})
        report_string += f"   Summary: {sign_def.get('summary', 'No summary available.')}\n\n"
    else:
        report_string += f"☉ Sun: Position Error or N/A\n\n"

    natal_moon_sign = chart_data.get("moon_sign", "N/A")
    moon_longitude = chart_data.get("planet_positions", {}).get("Moon", "N/A")
    if isinstance(moon_longitude, float):
        report_string += f"☽ Moon: {format_longitude(moon_longitude)} ({natal_moon_sign})\n"
        report_string += f"   Meaning: The Moon represents your emotional nature... In {natal_moon_sign}, this suggests... (add interpretation)\n\n"
    else:
        report_string += f"☽ Moon: Position Error or {natal_moon_sign}\n\n"

    asc_longitude = chart_data.get("ascendant_longitude", "N/A")
    if isinstance(asc_longitude, float):
        asc_sign = degree_to_sign(asc_longitude)
        report_string += (
            f"↑ Ascendant (Rising Sign): {format_longitude(asc_longitude)} ({asc_sign})\n"
        )
        report_string += f"   Meaning: Your Ascendant... In {asc_sign}, this means... (add interpretation)\n\n"
    else:
        report_string += f"↑ Ascendant: Calculation Error or N/A\n\n"

    # Add house reports
    report_string += "\n--- House Reports ---\n"
    for i in range(1, 13):  # Iterate through all 12 houses
        report_string += get_house_report_string(i) + "\n"

    report_string += "Planetary Placements:\n"
    planet_positions_data = chart_data.get(
        "planet_positions", {}
    )  # Use a different name to avoid conflict
    planet_houses = chart_data.get("planet_houses", {})

    # Use PLANET_LIST_FOR_REPORT defined in this module
    for planet_name, _ in PLANET_LIST_FOR_REPORT.items():  # Iterate using the local list
        lon_val = planet_positions_data.get(planet_name)  # Use _data suffixed variable
        house_num = planet_houses.get(planet_name)
        if isinstance(lon_val, float):
            sign = degree_to_sign(lon_val)
            report_string += (
                f"  {planet_name} in {sign} (House {house_num if house_num else 'N/A'}): {format_longitude(lon_val)}\n"
            )
        else:
            report_string += f"  {planet_name}: Position Error or N/A\n"
    report_string += "\n"

    report_string += "Key Aspects:\n"
    aspects_list = chart_data.get("aspects", [])
    if isinstance(aspects_list, list) and aspects_list:
        # Check if the first item is the placeholder info message
        if (
            isinstance(aspects_list[0], dict)
            and "info" in aspects_list[0]
            and "Placeholder" in aspects_list[0]["info"]
        ):
            report_string += f"  {aspects_list[0]['info']}\n"
        else:
            for aspect_info in aspects_list[:5]:
                p1 = aspect_info.get("planet1")
                asp_type = aspect_info.get("aspect_type")
                p2 = aspect_info.get("planet2")
                orb = aspect_info.get("orb")
                if p1 and asp_type and p2:
                    report_string += f"  - {p1} {asp_type} {p2} (Orb: {orb:.1f}°)\n"
                    report_string += get_aspect_report(asp_type)  # Add detailed aspect report
                else:
                    report_string += f"  - Incomplete aspect data: {aspect_info}\n"
    elif (
        isinstance(aspects_list, dict)
        and "info" in aspects_list
    ):  # Handle placeholder if aspects is a dict
        report_string += f"  {aspects_list['info']}\n"
    else:
        report_string += "  No significant aspects listed or error in calculation.\n"

    report_string += "\n--- End of Astrology Report ---\n"
    return report_string


if __name__ == "__main__":
    ephe_path_set = False
    try:
        # Ensure this path is correct for your system or use an environment variable
        eph_path = os.environ.get('SWEP_PATH', '/media/jeff/numy/numerology_ai/mp/')
        if os.path.isdir(eph_path):
            swe.set_ephe_path(eph_path)
            print(f"Swiss Ephemeris path set to: {eph_path}")
            ephe_path_set = True
        else:
            print(
                f"WARNING (astrology_report.py): Swiss Ephemeris directory not found at '{eph_path}'."
            )
    except Exception as e_eph:
        print(f"Error setting ephemeris path in astrology_report.py: {e_eph}")

    if ephe_path_set:
        print("\n--- Generating Sample Astrology Report ---")
        # Ensure birth_chart.py and its dependencies (planets.py, houses.py, aspects_calculater.py)
        # are correctly implemented in the .calculations subfolder.
        report = generate_astrology_report(
            1990, 3, 15, 14, 30, -74.0060, 40.7128, ut_offset=-5.0
        )
        print(report)
    else:
        print(
            "Skipping astrology report generation as ephemeris path is not set or other import errors occurred."
        )
