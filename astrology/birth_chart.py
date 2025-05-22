# /media/jeff/numy/numerology_ai/astrology/calculations/birth_chart.py

import swisseph as swe
import os # For setting ephe path in testing
import datetime # For date and time operations

# Relative imports:
# '.' means current package (which is 'calculations' when this file is part of it)
# '..' means parent package (which is 'astrology')
try:

    from .zodiac import get_moon_sign, degree_to_sign
    # Removed import of 'planet_positions' as it's not in zodiac.py
    # Removed circular import of 'calculate_aspects' from '.birth_chart'
    # The functions get_planet_positions, calculate_aspects, and assign_planets_to_houses
    # need to be defined in this file or imported from their correct modules.
except ImportError as e:
    print(f"Error importing modules within birth_chart.py: {e}")
    print("Ensure dependent files (aspects_calculater.py, planets.py, houses.py in 'calculations' and zodiac.py in 'astrology') exist and are correct.")
    # Define dummy functions if imports fail, so this module can still be imported partially
    def calculate_aspects(planet_positions): return {"error": "calculate_aspects not loaded"}
    def get_moon_sign(y,m,d,h,mi,lat,lon,alt=0): return "Error: get_moon_sign not loaded"
    def degree_to_sign(l): return "Error: degree_to_sign not loaded" # Updated dummy function name
    def get_planet_positions(y,m,d,h,mi,lat,lon,alt=0): return {"error": "get_planet_positions not loaded"}
    def assign_planets_to_houses(planet_positions, house_cusps): return {"error": "assign_planets_to_houses not loaded"}

def generate_birth_chart(year: int, month: int, day: int, hour: int = 12, minute: int = 0, ut_offset: float = 0.0, lat: float = 0.0, lon: float = 0.0, alt: float = 0):
    """
    Generate a complete birth chart.
    Time should ideally be provided in UT or with a UT offset for accuracy.
    """
    try:
        # Convert local time to Universal Time (UT)
        local_dt = datetime.datetime(year, month, day, hour, minute)
        ut_dt = local_dt - datetime.timedelta(hours=ut_offset)
        
        # Calculate Julian Day in UT using components from ut_dt
        jd_ut = swe.julday(ut_dt.year, ut_dt.month, ut_dt.day, 
                           ut_dt.hour + ut_dt.minute / 60.0 + ut_dt.second / 3600.0)

        # Set geographic position for topocentric calculations
        swe.set_topo(lon, lat, alt)

        # Get planet positions using UT date/time
        planet_positions = get_planet_positions(
            ut_dt.year, ut_dt.month, ut_dt.day, 
            ut_dt.hour, ut_dt.minute, 
            lat, lon, alt 
        )
        if "error" in planet_positions: 
            return {"error": f"Failed to get planet positions: {planet_positions['error']}"}

        # Get Moon Sign using UT date/time
        moon_sign = get_moon_sign(
            ut_dt.year, ut_dt.month, ut_dt.day, 
            ut_dt.hour, ut_dt.minute, 
            lat, lon, alt
        )
        if "Error" in moon_sign: 
             return {"error": f"Failed to get moon sign: {moon_sign}"}

        # Calculate aspects
        aspects = calculate_aspects(planet_positions) 
        if "error" in aspects: 
            return {"error": f"Failed to calculate aspects: {aspects['error']}"}

        # Calculate house cusps (Placidus by default) and Ascendant/MC
        house_cusps, ascmc = swe.houses(jd_ut, lat, lon, b'P') # Using Placidus ('P')

        # Assign planets to houses
        planet_houses = assign_planets_to_houses(planet_positions, list(house_cusps))
        if "error" in planet_houses: 
            return {"error": f"Failed to assign planets to houses: {planet_houses['error']}"}

        return {
            "birth_datetime_utc": ut_dt.strftime("%Y-%m-%d %H:%M:%S UT"),
            "julian_day_ut": jd_ut,
            "geo_location": {"latitude": lat, "longitude": lon, "altitude": alt},
            "planet_positions": planet_positions,
            "moon_sign": moon_sign,
            "aspects": aspects,
            "house_cusps_placidus": list(house_cusps), 
            "ascendant_longitude": ascmc[0],
            "mc_longitude": ascmc[1],
            "vertex_longitude": ascmc[3], 
            "planet_houses": planet_houses
        }
    except Exception as e:
        import traceback
        print(f"Error in generate_birth_chart (birth_chart.py): {e}")
        traceback.print_exc()
        return {"error": f"An unexpected error occurred in generating birth chart: {str(e)}"}

if __name__ == "__main__":
    # This block is for testing birth_chart.py directly
    print("Testing Birth Chart Generation (birth_chart.py)...")
    ephe_path_set = False
    try:
        eph_path = os.environ.get('SWEP_PATH', '/media/jeff/numy/numerology_ai/mp/') # Default if SWEP_PATH not set
        if eph_path and os.path.isdir(eph_path):
            swe.set_ephe_path(eph_path)
            print(f"Swiss Ephemeris path set to: {eph_path}")
            ephe_path_set = True
        else:
            print(f"WARNING (birth_chart.py test): Swiss Ephemeris directory not found at '{eph_path}'.")
        if not ephe_path_set:
             print("Please download ephemeris files and set the path using swe.set_ephe_path() or the SWEP_PATH environment variable for testing.")
    except Exception as e_eph:
        print(f"Error setting ephemeris path in birth_chart.py test: {e_eph}")

    if ephe_path_set:
        birth_data = {
            "year": 1990, "month": 3, "day": 15,
            "hour": 14, "minute": 30, "ut_offset": -5.0, 
            "lat": 40.7128, "lon": -74.0060 
        }
        print(f"\nGenerating chart for: {birth_data}")
        chart = generate_birth_chart(**birth_data)

        if "error" in chart:
            print(f"\n--- ERROR ---")
            print(chart["error"])
        else:
            print(f"\n--- Birth Chart Details (from birth_chart.py test) ---")
            print(f"Calculated for UTC: {chart.get('birth_datetime_utc')}")
            print(f"Moon Sign: {chart.get('moon_sign')}")
            print(f"Ascendant Longitude: {chart.get('ascendant_longitude'):.2f}")
            # Add more prints as needed
    else:
        print("Skipping birth chart test in birth_chart.py due to ephemeris path issue.")
