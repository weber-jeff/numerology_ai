# /media/jeff/numy/numerology_ai/astrology/zodiac.py

import datetime
import random
import pytz  # For timezone handling in get_julian_day
import swisseph as swe  # Import swisseph
import os  # Import the os module


# --- Basic Zodiac Sign Data ---
ZODIAC_SIGNS = {
    "Aries": {
        "start_month": 3,
        "start_day": 21,
        "end_month": 4,
        "end_day": 19,
        "element": "Fire",
        "modality": "Cardinal",
        "symbol": "♈",
        "longitude_start": 0,
    },
    "Taurus": {
        "start_month": 4,
        "start_day": 20,
        "end_month": 5,
        "end_day": 20,
        "element": "Earth",
        "modality": "Fixed",
        "symbol": "♉",
        "longitude_start": 30,
    },
    "Gemini": {
        "start_month": 5,
        "start_day": 21,
        "end_month": 6,
        "end_day": 20,
        "element": "Air",
        "modality": "Mutable",
        "symbol": "♊",
        "longitude_start": 60,
    },
    "Cancer": {
        "start_month": 6,
        "start_day": 21,
        "end_month": 7,
        "end_day": 22,
        "element": "Water",
        "modality": "Cardinal",
        "symbol": "♋",
        "longitude_start": 90,
    },
    "Leo": {
        "start_month": 7,
        "start_day": 23,
        "end_month": 8,
        "end_day": 22,
        "element": "Fire",
        "modality": "Fixed",
        "symbol": "♌",
        "longitude_start": 120,
    },
    "Virgo": {
        "start_month": 8,
        "start_day": 23,
        "end_month": 9,
        "end_day": 22,
        "element": "Earth",
        "modality": "Mutable",
        "symbol": "♍",
        "longitude_start": 150,
    },
    "Libra": {
        "start_month": 9,
        "start_day": 23,
        "end_month": 10,
        "end_day": 22,
        "element": "Air",
        "modality": "Cardinal",
        "symbol": "♎",
        "longitude_start": 180,
    },
    "Scorpio": {
        "start_month": 10,
        "start_day": 23,
        "end_month": 11,
        "end_day": 21,
        "element": "Water",
        "modality": "Fixed",
        "symbol": "♏",
        "longitude_start": 210,
    },
    "Sagittarius": {
        "start_month": 11,
        "start_day": 22,
        "end_month": 12,
        "end_day": 21,
        "element": "Fire",
        "modality": "Mutable",
        "symbol": "♐",
        "longitude_start": 240,
    },
    "Capricorn": {
        "start_month": 12,
        "start_day": 22,
        "end_month": 1,
        "end_day": 19,
        "element": "Earth",
        "modality": "Cardinal",
        "symbol": "♑",
        "longitude_start": 270,
    },
    "Aquarius": {
        "start_month": 1,
        "start_day": 20,
        "end_month": 2,
        "end_day": 18,
        "element": "Air",
        "modality": "Fixed",
        "symbol": "♒",
        "longitude_start": 300,
    },
    "Pisces": {
        "start_month": 2,
        "start_day": 19,
        "end_month": 3,
        "end_day": 20,
        "element": "Water",
        "modality": "Mutable",
        "symbol": "♓",
        "longitude_start": 330,
    },
}
SIGN_ORDER = [
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces",
]

# --- Planet Names (as expected by astrology_report.py) ---
PLANET_NAMES = {  # Map swisseph indices to names
    swe.SUN: "Sun",
    swe.MOON: "Moon",
    swe.MERCURY: "Mercury",
    swe.VENUS: "Venus",
    swe.MARS: "Mars",
    swe.JUPITER: "Jupiter",
    swe.SATURN: "Saturn",
    swe.URANUS: "Uranus",
    swe.NEPTUNE: "Neptune",
    swe.PLUTO: "Pluto",
}

# --- Aspect Definitions (as expected by astrology_report.py) ---
ASPECT_ANGLES = {  # Angle: Name
    0: "Conjunction",
    180: "Opposition",
    120: "Trine",
    90: "Square",
    60: "Sextile",
}

ASPECT_TYPES = {  # Name: Type (Harmonious/Challenging) - Simplified
    "Conjunction": "Neutral",
    "Opposition": "Challenging",
    "Trine": "Harmonious",
    "Square": "Challenging",
    "Sextile": "Harmonious",
}


def get_sun_sign(birth_month: int, birth_day: int) -> str:
    """Determines the Zodiac Sun Sign based on month and day."""
    for sign, data in ZODIAC_SIGNS.items():
        if data["start_month"] > data["end_month"]:  # Spans new year
            if (
                birth_month == data["start_month"] and birth_day >= data["start_day"]
            ) or (birth_month == data["end_month"] and birth_day <= data["end_day"]):
                return sign
        else:
            if (
                data["start_month"] == birth_month and birth_day >= data["start_day"]
            ) or (
                data["end_month"] == birth_month and birth_day <= data["end_day"]
            ) or (data["start_month"] < birth_month < data["end_month"]):
                return sign
    # Fallback logic for cusp dates (simplified)
    if (birth_month == 12 and birth_day >= 22) or (
        birth_month == 1 and birth_day <= 19
    ):
        return "Capricorn"
    if (birth_month == 1 and birth_day >= 20) or (
        birth_month == 2 and birth_day <= 18
    ):
        return "Aquarius"
    # Add more specific cusp handling if needed, or rely on longitude based methods for precision
    return "Unknown Sign"


# Renamed to match import in astrology_report.py
def degree_to_sign(longitude: float) -> str:
    """Determines the zodiac sign from a given ecliptic longitude."""
    # Normalize longitude to 0-359.999 degrees
    longitude = longitude % 360
    for sign_name in SIGN_ORDER:
        data = ZODIAC_SIGNS[sign_name]
        start_lon = data["longitude_start"]
        end_lon = (start_lon + 30) % 360
        if start_lon < end_lon:  # Normal case (e.g., Aries 0-30)
            if start_lon <= longitude < end_lon:
                return sign_name
        else:  # Wraps around 360 (e.g. Pisces 330-0/360)
            if start_lon <= longitude < 360 or 0 <= longitude < end_lon:
                return sign_name
    return "Unknown Sign (Longitude Error)"


# --- Julian Day Calculation ---
def get_julian_day(
    year: int,
    month: int,
    day: int,
    hour: int = 12,
    minute: int = 0,
    second: int = 0,
    timezone_str: str = "UTC",
) -> float:
    """Calculate Julian Day number for a given date/time, with timezone handling."""
    try:
        local_tz = pytz.timezone(timezone_str)
    except pytz.exceptions.UnknownTimeZoneError:
        # Fallback to UTC if timezone string is invalid
        print(f"Warning: Unknown timezone '{timezone_str}'. Defaulting to UTC.")
        local_tz = pytz.utc

    # Create a naive datetime object first
    naive_dt = datetime.datetime(year, month, day, hour, minute, second)

    # Localize the naive datetime object to the specified timezone
    localized_dt = local_tz.localize(naive_dt)

    # Convert the localized datetime to UTC
    utc_dt = localized_dt.astimezone(pytz.utc)

    # Calculate Julian Day from UTC datetime components
    jd = swe.julday(
        utc_dt.year,
        utc_dt.month,
        utc_dt.day,
        utc_dt.hour + utc_dt.minute / 60.0 + utc_dt.second / 3600.0,
    )
    return jd


def get_moon_sign(
    year: int,
    month: int,
    day: int,
    hour: int = 12,
    minute: int = 0,
    lat: float = 0.0,
    lon: float = 0.0,
    alt: float = 0,
    timezone_str: str = "UTC",
) -> str:
    """
    Calculates the Moon's zodiac sign for a given date, time, and location.
    Args:
        year (int): Year of birth/event.
        month (int): Month of birth/event.
        day (int): Day of birth/event.
        hour (int): Hour of birth/event (local time). Default 12.
        minute (int): Minute of birth/event. Default 0.
        lat (float): Latitude of location. Default 0.0.
        lon (float): Longitude of location. Default 0.0.
        alt (float): Altitude of location in meters. Default 0.
        timezone_str (str): Timezone string (e.g., "America/New_York"). Default "UTC".
    Returns:
        str: The zodiac sign of the Moon, or "Error calculating Moon sign".
    """
    try:
        # Calculate Julian Day in UT using timezone
        jd_ut = get_julian_day(year, month, day, hour, minute, 0, timezone_str)

        # Set geographic position for topocentric calculations (more precise for Moon)
        swe.set_topo(lon, lat, alt)

        # Calculate Moon's position.
        # swe.MOON is the planet index for the Moon.
        # swe.FLG_SWIEPH for Swiss Ephemeris, swe.FLG_SPEED for speed, swe.FLG_TOPOCTR for topocentric
        moon_data = swe.calc_ut(jd_ut, swe.MOON, swe.FLG_SWIEPH | swe.FLG_SPEED)

        if not moon_data or len(moon_data[0]) == 0:
            return "Error: Could not calculate Moon position."

        moon_longitude = moon_data[0][0]  # Ecliptic longitude

        return degree_to_sign(moon_longitude)

    except Exception as e:
        print(f"Error in get_moon_sign: {e}")  # Log this error
        return "Error calculating Moon sign"


def get_sign_details(sign_name: str) -> dict:
    return ZODIAC_SIGNS.get(sign_name, {})


# --- Element and Modality Functions (as expected by astrology_report.py) ---
def element(sign_name: str) -> str:
    """Returns the element of a given zodiac sign."""
    sign_info = ZODIAC_SIGNS.get(sign_name, {})
    return sign_info.get("element", "Unknown Element")


def modality(sign_name: str) -> str:
    """Returns the modality of a given zodiac sign."""
    sign_info = ZODIAC_SIGNS.get(sign_name, {})
    return sign_info.get("modality", "Unknown Modality")


# --- Aspect Calculation Function (as expected by astrology_report.py) ---
def calculate_aspects_within_chart(planet_positions: dict, orb: float = 6.0) -> list:
    """
    Calculate aspects between planet positions within a single chart.
    Assumes planet_positions is a dict like {"Sun": 123.45, "Moon": 67.89, ...}
    Returns: list of strings representing aspects, e.g., ["Sun Trine Moon (orb 1.23)"]
             or a list of dictionaries for more structured data.
    """
    aspects_found = []
    planets = list(planet_positions.keys())
    num_planets = len(planets)

    for i in range(num_planets):
        for j in range(i + 1, num_planets):  # Avoid self-aspects and duplicate pairs
            p1_name = planets[i]
            p2_name = planets[j]

            pos1 = planet_positions.get(p1_name)
            pos2 = planet_positions.get(p2_name)

            if pos1 is None or pos2 is None:  # Skip if a planet's position is missing
                continue

            angle_diff = abs(pos1 - pos2)
            if angle_diff > 180:
                angle_diff = 360 - angle_diff

            for aspect_angle, aspect_name in ASPECT_ANGLES.items():
                current_orb = abs(angle_diff - aspect_angle)
                if current_orb <= orb:
                    # Simple string representation for now, matches prior expectation
                    aspects_found.append(
                        f"{p1_name} {aspect_name} {p2_name} (orb {current_orb:.2f})"
                    )
                    break  # Found the tightest aspect for this pair
    return aspects_found


# --- Daily Astrological Influences Function (Dummy Implementation from previous version) ---
def get_astrological_influences(
    user_birth_details: dict, target_date_obj: datetime.date
) -> dict:
    """
    Provides dummy daily astrological influences based on the transiting Moon.
    This is a placeholder implementation and should be replaced with a more
    accurate and meaningful calculation.
    """
    # For a real daily influence, you'd typically use a standard time like noon UT for the target day,
    # and a generic location or 0,0 lat/lon if not specific to a user's location.
    dummy_moon_sign = get_moon_sign(
        target_date_obj.year,
        target_date_obj.month,
        target_date_obj.day,
        timezone_str="UTC",  # Use UTC for general daily influences
        # hour, minute, lat, lon could be standardized for general daily influences
    )
    if "Error" in dummy_moon_sign:  # Handle potential error from get_moon_sign
        all_signs = list(ZODIAC_SIGNS.keys())
        day_of_year = target_date_obj.timetuple().tm_yday
        moon_sign_index = (day_of_year // 2) % len(all_signs)
        dummy_moon_sign = all_signs[moon_sign_index]

    month = target_date_obj.month
    day = target_date_obj.day
    dummy_mercury_retrograde = False
    if (month == 1 and 1 <= day <= 20) or (month == 4 and 10 <= day <= 30) or (
        month == 8 and 15 <= day <= 31
    ) or (month == 9 and 1 <= day <= 5) or (month == 12 and 1 <= day <= 20):
        dummy_mercury_retrograde = True

    moon_sign_details_today = get_sign_details(dummy_moon_sign)
    dummy_dominant_element = moon_sign_details_today.get(
        "element", random.choice(["Fire", "Earth", "Air", "Water"])
    )
    dummy_dominant_modality = moon_sign_details_today.get(
        "modality", random.choice(["Cardinal", "Fixed", "Mutable"])
    )

    dummy_harmonious_transits = random.randint(0, 5)
    dummy_challenging_transits = random.randint(0, 4)

    categories = [
        "Dynamic",
        "Stable",
        "Growth",
        "Challenge",
        "Social",
        "Emotional",
        "Detailed",
        "Creative",
        "Reflective",
        "Productive",
    ]
    if dummy_mercury_retrograde and dummy_challenging_transits > 2:
        dummy_key_category = random.choice(["Reflective Challenge", "Detailed Review"])
    elif (
        dummy_harmonious_transits > dummy_challenging_transits + 1
        and not dummy_mercury_retrograde
    ):
        dummy_key_category = random.choice(
            ["Productive Growth", "Dynamic Flow", "Social Harmony"]
        )
    elif dummy_challenging_transits > dummy_harmonious_transits + 1:
        dummy_key_category = random.choice(["Challenge", "Emotional Test"])
    else:
        dummy_key_category = random.choice(categories)

    return {
        "transiting_moon_sign": dummy_moon_sign,
        "mercury_retrograde": dummy_mercury_retrograde,
        "dominant_element_today": dummy_dominant_element,
        "dominant_modality_today": dummy_dominant_modality,
        "harmonious_transit_count": dummy_harmonious_transits,
        "challenging_transit_count": dummy_challenging_transits,
        "key_transit_category": dummy_key_category,
    }


if __name__ == "__main__":
    print("--- Testing Zodiac Functions ---")
    # Set ephemeris path for testing if running this file directly
    # You need to download ephemeris files (e.g., sepl_18.se1, semo_18.se1)
    # and place them in a directory.
    try:
        # Try to set a common path, or instruct user.
        # This path needs to point to where your Swiss Ephemeris files are stored.
        swe.set_ephe_path(
            os.environ.get("SWEP_PATH", ".")
        )  # Check env var or current dir
    except Exception as e:
        print(
            f"Could not set ephemeris path. Place ephemeris files in a directory and set path via swe.set_ephe_path() or SWEP_PATH env var. Error: {e}"
        )

    print(f"Sun sign for May 15: {get_sun_sign(5, 15)}")
    print(f"Sun sign for Dec 25: {get_sun_sign(12, 25)}")

    print("\n--- Testing get_moon_sign ---")
    # Note: For accurate Moon signs, time (UT) and location are important.
    # These examples use default time (noon) and location (0,0).
    print(f"Moon sign for 1990-03-15 (default time/loc): {get_moon_sign(1990, 3, 15)}")
    print(f"Moon sign for 2023-10-26 (default time/loc): {get_moon_sign(2023, 10, 26)}")
    # For a specific time and location (e.g., New York approx -5 UT offset from GMT)
    # 14:30 Local Time in NY
    print(
        f"Moon sign for 1990-03-15, 14:30, NY (lat 40.7, lon -74.0, tz=America/New_York): {get_moon_sign(1990, 3, 15, hour=14, minute=30, lat=40.7128, lon=-74.0060, timezone_str='America/New_York')}"
    )

    print(
        "\n--- Testing Daily Astrological Influences (uses get_moon_sign for dummy transiting moon) ---"
    )
    today = datetime.date.today()
    influences_today = get_astrological_influences(
        {}, today
    )  # Pass empty dict for birth_details as it's not used by dummy
    for key, value in influences_today.items():
        print(f"  {key}: {value}")
