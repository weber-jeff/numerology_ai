# /media/jeff/numy/numerology_ai/numerology/numerology_report.py
import os
import sys
import datetime # For get_numerological_insights and __main__ examples
from collections import Counter # For Hidden Passion
from datetime import datetime
# --- Section 1: Setup for Importing Compatibility Data (SIMPLIFIED) ---
# Now we only need to import one comprehensive dictionary from combat1.py

# This variable will hold your single, comprehensive compatibility dictionary
all_life_path_compat_data = None 
try:
    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    n_combat_dir_to_add = os.path.join(current_script_directory, "n_combat")

    if n_combat_dir_to_add not in sys.path:
        sys.path.insert(0, n_combat_dir_to_add)
        print(f"DEBUG: Added '{n_combat_dir_to_add}' to sys.path")
    # else: # Good for debugging
        # print(f"DEBUG: '{n_combat_dir_to_add}' already in sys.path")

    # Attempt to import the single comprehensive compatibility dictionary
    try:
        from n_combat.combat1 import life_path_compatibility # Assuming the dict in combat1.py is named this
        all_life_path_compat_data = life_path_compatibility
        print("SUCCESS: Imported comprehensive Life Path compatibility data from combat1.py.")
    except ImportError:
        print("ERROR: Could not import Life Path compatibility data from n_combat/combat1.py. File not found or dictionary name incorrect.")
        all_life_path_compat_data = {} # Initialize as empty dict to prevent errors later if import fails
    except Exception as e:
        print(f"ERROR importing compatibility data from combat1.py: {e}")
        all_life_path_compat_data = {}

except Exception as e:
    print(f"ERROR during initial setup of compatibility data imports: {e}")
    all_life_path_compat_data = {}


# --- Section 2: Core Numerology Calculation Logic ---
# (This section remains the same: PYTHAGOREAN_MAP, VOWELS, reduce_number, 
#  calculate_life_path, calculate_expression_number, etc. ...
#  get_reduced_date_components, calculate_balance_number, calculate_maturity_number,
#  calculate_challenge_numbers, calculate_pinnacle_numbers, calculate_hidden_passion_number)
# For brevity, not re-pasting all these functions here. Ensure they are present.
# --- Letter to Number Mappings (Standardized) ---
PYTHAGOREAN_MAP = {
    'A': 1, 'J': 1, 'S': 1,
    'B': 2, 'K': 2, 'T': 2,
    'C': 3, 'L': 3, 'U': 3,
    'D': 4, 'M': 4, 'V': 4,
    'E': 5, 'N': 5, 'W': 5,
    'F': 6, 'O': 6, 'X': 6,
    'G': 7, 'P': 7, 'Y': 7,
    'H': 8, 'Q': 8, 'Z': 8,
    'I': 9, 'R': 9
}

VOWELS = "AEIOU"

# --- Helper Functions ---
def reduce_number(n: int, keep_master_as_is=True) -> int:
    """Reduces a number to a single digit or a master number (11, 22, 33)."""
    if keep_master_as_is and n in [11, 22, 33]: return n
    s = str(n)
    while len(s) > 1:
        current_sum = sum(int(digit) for digit in s)
        if keep_master_as_is and current_sum in [11, 22, 33] and len(str(current_sum)) == 2:
            return current_sum
        s = str(current_sum)
        if len(s) == 1: break
    return int(s)

def numerology_reduce(n: int) -> int:
    """Reduces a number to a single digit unless it's a master number."""
    while n > 9 and n not in (11, 22, 33):
        n = sum(int(digit) for digit in str(n))
    return n

def get_number_from_string(text: str, letter_map: dict) -> int:
    """Calculates the sum of numerical values of letters in a string."""
    total = 0
    for char in text.upper():
        if char in letter_map:
            total += letter_map[char]
    return total

def calculate_life_path(birth_date_str: str) -> int:
    """Calculates the life path number from a birth date string (YYYY-MM-DD)."""
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        year = birth_date.year
        month = birth_date.month
        day = birth_date.day
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return 0

    year_sum = sum_digits(year)
    month_sum = sum_digits(month)
    day_sum = sum_digits(day)

    life_path = sum_digits(year_sum + month_sum + day_sum)
    return life_path

def sum_digits(n: int) -> int:
    """Sums the digits of a number until a single digit is obtained."""
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

def calculate_expression_number(full_name_str):
    """Calculates the Expression (Destiny) number from the full birth name."""
    try:
        name_for_calc = "".join(filter(str.isalpha, full_name_str))
        if not name_for_calc:
            return "Name Required"
        name_sum = get_number_from_string(name_for_calc, PYTHAGOREAN_MAP)
        return reduce_number(name_sum)
    except Exception as e:
        print(f"Error in calculate_expression_number: {e}")
        return "Error"

def calculate_soul_urge_number(full_name_str):
    """Calculates the Soul Urge (Heart's Desire) number from vowels in the name."""
    try:
        name_for_calc = "".join(filter(str.isalpha, full_name_str))
        vowel_str = "".join(char for char in name_for_calc.upper() if char in VOWELS)
        if not vowel_str:
            return 0  # Or a specific string like "No Vowels"
        vowel_sum = get_number_from_string(vowel_str, PYTHAGOREAN_MAP)
        return reduce_number(vowel_sum)
    except Exception as e:
        print(f"Error in calculate_soul_urge_number: {e}")
        return "Error"

def calculate_personality_number(full_name_str):
    """Calculates the Personality number from consonants in the name."""
    try:
        name_for_calc = "".join(filter(str.isalpha, full_name_str))
        consonant_str = "".join(char for char in name_for_calc.upper() if char not in VOWELS)
        if not consonant_str:
            return 0  # Or a specific string like "No Consonants"
        consonant_sum = get_number_from_string(consonant_str, PYTHAGOREAN_MAP)
        return reduce_number(consonant_sum)
    except Exception as e:
        print(f"Error in calculate_personality_number: {e}")
        return "Error"

def calculate_birthday_number(birth_date_str):
    """Calculates the Birthday Number from the day of birth."""
    try:
        day_str = birth_date_str.split('-')[2]
        return reduce_number(int(day_str))
    except (ValueError, IndexError):
        return "Invalid Date Format"
    except Exception as e:
        print(f"Error in calculate_birthday_number: {e}")
        return "Error"
def get_reduced_date_components(birth_date_str: str) -> tuple[int|str, int|str, int|str] | str:
    try:
        parts = birth_date_str.split('-')
        if len(parts) != 3: raise ValueError("Date must be YYYY-MM-DD")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        r_month = reduce_number(month, keep_master_as_is=True)
        r_day = reduce_number(day, keep_master_as_is=True)
        year_sum_digits = sum(int(d) for d in str(year))
        r_year = reduce_number(year_sum_digits, keep_master_as_is=True)
        return r_month, r_day, r_year
    except ValueError as ve: return f"Invalid date component: {ve}"
    except Exception as e: return f"Error reducing date components: {e}"
def calculate_balance_number(full_name_str: str) -> int | str:
    try:
        name_parts = full_name_str.upper().split()
        if not name_parts: return "Name Required"
        initials_sum = 0
        for part in name_parts:
            if part and part[0].isalpha() and part[0] in PYTHAGOREAN_MAP:
                initials_sum += PYTHAGOREAN_MAP[part[0]]
        if initials_sum == 0 and full_name_str: return "Could not derive initials"
        elif initials_sum == 0 and not full_name_str: return "Name Required"
        return reduce_number(initials_sum)
    except Exception as e: return f"Error calculating Balance Number: {e}"
def calculate_maturity_number(life_path_num: int, expression_num: int) -> int | str:
    if not (isinstance(life_path_num, int) and isinstance(expression_num, int)):
        return "Valid Life Path and Expression numbers required"
    maturity_sum = life_path_num + expression_num
    return reduce_number(maturity_sum)
def calculate_challenge_numbers(birth_date_str: str) -> list[int | str] | str:
    components = get_reduced_date_components(birth_date_str)
    if isinstance(components, str): return f"Cannot calculate Challenges: {components}"
    r_month, r_day, r_year = components
    sd_month = reduce_number(r_month, keep_master_as_is=False)
    sd_day = reduce_number(r_day, keep_master_as_is=False)
    sd_year = reduce_number(r_year, keep_master_as_is=False)
    if not all(isinstance(i, int) for i in [sd_month, sd_day, sd_year]):
         return "Invalid date components for Challenges after reduction."
    try:
        challenge1 = reduce_number(abs(sd_month - sd_day), keep_master_as_is=False)
        challenge2 = reduce_number(abs(sd_day - sd_year), keep_master_as_is=False)
        main_challenge3 = reduce_number(abs(challenge1 - challenge2), keep_master_as_is=False)
        challenge4 = reduce_number(abs(sd_month - sd_year), keep_master_as_is=False)
        return [challenge1, challenge2, main_challenge3, challenge4]
    except Exception as e: return f"Error calculating Challenges: {e}"
def calculate_pinnacle_numbers(birth_date_str: str) -> list[int | str] | str:
    components = get_reduced_date_components(birth_date_str)
    if isinstance(components, str): return f"Cannot calculate Pinnacles: {components}"
    r_month, r_day, r_year = components
    if not all(isinstance(i, int) for i in [r_month, r_day, r_year]):
         return "Invalid date components for Pinnacles."
    try:
        pinnacle1 = reduce_number(r_month + r_day)
        pinnacle2 = reduce_number(r_day + r_year)
        pinnacle3 = reduce_number(pinnacle1 + pinnacle2)
        pinnacle4 = reduce_number(r_month + r_year)
        return [pinnacle1, pinnacle2, pinnacle3, pinnacle4]
    except Exception as e: return [f"Error calculating Pinnacles: {e}"] * 4 # Return list of errors

def calculate_hidden_passion_number(full_name_str: str) -> int | str:
    """Calculates the Hidden Passion number (sum of most frequent digits, reduced)."""
    try:
        name_for_calc = "".join(filter(str.isalpha, full_name_str)).upper()
        if not name_for_calc: return "Name Required"

        all_digits_in_name = [PYTHAGOREAN_MAP[char] for char in name_for_calc if char in PYTHAGOREAN_MAP]
        if not all_digits_in_name: return "No valid letters for Hidden Passion calculation"

        digit_counts = Counter(all_digits_in_name)
        if not digit_counts: return "No digits found in name for Hidden Passion"

        max_freq = max(digit_counts.values())
        most_frequent_digits = [num for num, count in digit_counts.items() if count == max_freq]

        if not most_frequent_digits:
            return "No dominant digit found for Hidden Passion"
        
        hidden_passion_sum = sum(most_frequent_digits)
        return reduce_number(hidden_passion_sum)
    except Exception as e: return f"Error calculating Hidden Passion: {e}"
    
def calculate_karmic_lesson_number(full_name_str: str) -> int | str:
    """Calculates the Karmic Lesson number from the name."""
    try:
        name_for_calc = "".join(filter(str.isalpha, full_name_str)).upper()
        if not name_for_calc: return "Name Required for Karmic Lesson"
        present_digits = {PYTHAGOREAN_MAP[char] for char in name_for_calc if char in PYTHAGOREAN_MAP}
        for i in range(1, 10): # Check for missing digits 1 through 9
            if i not in present_digits:
                return i
        return 0  # All digits 1-9 are present
    except Exception as e: return f"Error calculating Karmic Lesson: {e}"

def calculate_personal_number(birth_date_str: str) -> int:
    """Calculates the personal number from the birth date."""
    # Extract the month and day from the birth date string
    try:
        month = int(birth_date_str.split('-')[1])
        day = int(birth_date_str.split('-')[2])
        personal_number = month + day
        personal_number = personal_number % 33
        if personal_number == 0:
            personal_number = 33  # Ensure the number is within 1-33
        print(f"DEBUG: calculate_personal_number - month: {month}, day: {day}, personal_number: {personal_number}")  # Debugging
        return personal_number
    except (ValueError, IndexError):
        print("DEBUG: Invalid birth date format in calculate_personal_number")  # Debugging
        return 0  # Handle invalid birth date format

def calculate_personal_numbers(birth_month: int, birth_day: int, year: int, month: int, day: int) -> dict:
    birth_sum = numerology_reduce(birth_month + birth_day)
    year_sum = numerology_reduce(sum(int(d) for d in str(year)))
    personal_year = reduce_number(birth_sum + year_sum)
    personal_month = reduce_number(personal_year + month)
    personal_day = reduce_number(personal_month + day)

    return {
        "Personal Year": personal_year,
        "Personal Month": personal_month,
        "Personal Day": personal_day
    }

# --- Section 3: Daily Insights Functions ---
# (This section remains the same)
# For brevity, not re-pasting. Ensure it's present.
def reduce_number_simple(n):
    s = str(n)
    while len(s) > 1: s = str(sum(int(digit) for digit in s))
    return int(s)
def get_numerological_insights(birth_month, birth_day, target_date_obj):
    try:
        personal_day = reduce_number_simple(birth_month + birth_day + target_date_obj.day)
        personal_month = reduce_number_simple(birth_month + target_date_obj.month)
        personal_year = reduce_number_simple(birth_month + birth_day + target_date_obj.year)
        personal_day_meaning = f"Energy of {personal_day}. Themes: [to be defined for {personal_day}]"
        return {
            "personal_day": f"{personal_day} ({personal_day_meaning})",
            "personal_month": str(personal_month), "personal_year": str(personal_year),
        }
    except Exception as e: return {"personal_day": "Error calculating daily insights", "error_message": str(e)}


# --- Section 4: Interpretation Dictionaries ---
# (This section remains the same: life_path_meanings, get_life_path_meaning,
#  placeholders for EXPRESSION_INTERPRETATIONS, SOUL_URGE_INTERPRETATIONS, etc.)
# For brevity, not re-pasting. Ensure it's present.
life_path_meanings = { 1: {"description": "Independent...", "advice": "...", "master": False, "element": "Fire", "traits": [], "strengths": [], "weaknesses": []},
    11: {"description": "Intuitive...", "advice": "...", "master": True, "element": "Air", "traits": [], "strengths": [], "weaknesses": []},} # Populate fully
DEFAULT_LP_MEANING = { "description": "Life Path meaning not found.", "advice": "N/A", "master": False, "element": "N/A", "traits": [], "strengths": [], "weaknesses": []}
def get_life_path_meaning(number: int) -> dict: return life_path_meanings.get(number, DEFAULT_LP_MEANING)
EXPRESSION_INTERPRETATIONS = {1: "Expression 1 meaning..."} # Populate fully
SOUL_URGE_INTERPRETATIONS = {1: "Soul Urge 1 meaning..."} # Populate fully
PERSONALITY_INTERPRETATIONS = {1: "Personality 1 meaning..."} # Populate fully
BIRTHDAY_INTERPRETATIONS = {1: "Birthday 1 meaning..."} # Populate fully
BALANCE_NUMBER_INTERPRETATIONS = {1: "Balance Number 1 meaning..."} # Populate fully
MATURITY_NUMBER_INTERPRETATIONS = {1: "Maturity Number 1 meaning..."} # Populate fully
CHALLENGE_NUMBER_INTERPRETATIONS = {0: "Challenge 0 meaning..."} # Populate fully
PINNACLE_NUMBER_INTERPRETATIONS = {1: "Pinnacle 1 meaning..."} # Populate fully
HIDDEN_PASSION_INTERPRETATIONS = {1: "Hidden Passion for 1..."} # Populate fully
DEFAULT_INTERPRETATION = "Interpretation pending."
DEFAULT_BALANCE_MEANING = {"description": "Balance Number meaning not found.", "advice": "N/A"}
def get_balance_meaning(number: int) -> dict: return BALANCE_NUMBER_INTERPRETATIONS.get(number, DEFAULT_BALANCE_MEANING)


# --- Section 5: Main Report Generation Function ---
# (This function generate_full_numerology_report remains largely the same in structure,
#  it will just use the new way of getting compatibility below if it were to call it,
#  but its primary role is the blueprint, not compatibility between two people)
# For brevity, not re-pasting the full generate_full_numerology_report. Ensure it's present.
def generate_full_numerology_report(name: str, birth_date_str: str) -> str:
    # ... (previous implementation that calculates all numbers and formats them) ...
    # This function calculates and formats the single person blueprint.
    # It does NOT use the life_path_compatibility dictionary directly.
    # It uses life_path_meanings for the individual's LP.
    # (Ensure this function is complete as per previous versions)
    # Example snippet of how it uses get_life_path_meaning:
    lp_num = calculate_life_path(birth_date_str)
    if not isinstance(lp_num, int): return f"Could not calculate Life Path: {lp_num}"
    lp_details = get_life_path_meaning(lp_num)
    lp_report_section_intro = [
        "--------------------------------------------------",
        "🔑 THE LIFE PATH NUMBER (General Meaning)",
        "--------------------------------------------------",
        "The Life Path number is often considered the most significant number in your numerology chart...",
        "\n"
    ]
    lp_report_section_details = [
        f"🔑 LIFE PATH NUMBER: {lp_num} {'(Master Number)' if lp_details.get('master') else ''}",
        f"   Element: {lp_details.get('element', 'N/A')}",
        "--------------------------------------------------",
        f"Description: {lp_details.get('description', DEFAULT_INTERPRETATION)}",
        # ... more details from lp_details ...
        "\n"
    ]
    # This is just a small part of generate_full_numerology_report
    # The full function as defined before should be here.
    # For this example, let's assume it's defined elsewhere or copy-pasted fully.
    # For now, a placeholder:
    if 'generate_full_numerology_report_defined_elsewhere' not in locals():
        def generate_full_numerology_report(name, birth_date_str):
            # THIS IS A PLACEHOLDER - USE YOUR FULL FUNCTION
            lp_num = calculate_life_path(birth_date_str)
            if not isinstance(lp_num, int): return f"Error in LP calc: {lp_num}"
            lp_details = get_life_path_meaning(lp_num)
            return (f"Report for {name} ({birth_date_str}):\n"
                    f"Life Path: {lp_num} - {lp_details.get('description')}\n"
                    f"... other numbers ...")


# --- Section 6: Life Path Compatibility Report Function (UPDATED) ---
def get_compatibility_meaning(num1: int, num2: int) -> str:
    """
    Return compatibility meaning for a pair of numbers using the single 
    comprehensive 'all_life_path_compat_data' dictionary.
    """
    if all_life_path_compat_data is None or not all_life_path_compat_data: # Check if data loaded
        return "Life Path compatibility data is not loaded or is empty."

    # Normalize the pair to ensure smaller number is first, as per typical dictionary structure
    key_pair = tuple(sorted((num1, num2))) 
    
    meaning = all_life_path_compat_data.get(key_pair)
    
    if meaning:
        return meaning.strip()
    else:
        # Try reversing if your dictionary might not be strictly ordered (though it should be)
        # key_pair_reversed = (num2, num1) 
        # meaning_reversed = all_life_path_compat_data.get(key_pair_reversed)
        # if meaning_reversed:
        #     return meaning_reversed.strip()
        return f"No specific compatibility meaning found for the pair ({num1}, {num2}). Ensure the pair {key_pair} exists in combat1.py."

def generate_life_path_compatibility_output(person1_name, person1_dob_str, person2_name, person2_dob_str):
    lp1 = calculate_life_path(person1_dob_str)
    lp2 = calculate_life_path(person2_dob_str)

    if not (isinstance(lp1, int) and isinstance(lp2, int)):
        errors = []
        if not isinstance(lp1, int): errors.append(f"{person1_name} LP Error: {lp1}")
        if not isinstance(lp2, int): errors.append(f"{person2_name} LP Error: {lp2}")
        return f"Could not calculate Life Paths for compatibility. Details: {'; '.join(errors)}"

    output = [f"\n--- Life Path Compatibility: {person1_name} (LP {lp1}) & {person2_name} (LP {lp2}) ---"]
    compatibility_text = get_compatibility_meaning(lp1, lp2)
    output.append(compatibility_text)
    
    return "\n".join(output)


# --- Section 7: Main Execution Block ---
if __name__ == '__main__':
    print("--- Numerology Report Script Initialized ---")
    if not all_life_path_compat_data: # Check if compatibility data actually loaded
        print("WARNING: The comprehensive Life Path compatibility dictionary (from combat1.py) was not loaded. Compatibility reports will be limited.")

    # --- Test Full Numerology Blueprint ---
    # Ensure generate_full_numerology_report is fully defined above or imported
    test_name = "Jeffery Allen Louis Weber"
    test_birth_date = "1987-05-08" 
    print(f"\n--- Generating Full Blueprint for {test_name} ({test_birth_date}) ---")
    # You need the full definition of generate_full_numerology_report here from previous steps
    # For now, assuming it's defined and just calling it:
    if 'generate_full_numerology_report_defined_elsewhere' in locals(): # Check if it's the placeholder
         print("NOTE: Using placeholder for generate_full_numerology_report. For full output, ensure it's completely defined.")
    full_report = generate_full_numerology_report(test_name, test_birth_date)
    print(full_report)

    # --- Test Life Path Compatibility using the single comprehensive dictionary ---
    # Example: LP 1 and LP 5 (assuming (1,5) key exists in your combat1.py)
    # LP1: 1970-01-01 -> LP 1
    # LP5: 1970-05-01 -> LP 5
    compatibility_output = generate_life_path_compatibility_output(
        person1_name="Pioneer One", person1_dob_str="1970-01-01",
        person2_name="Adventurer Five", person2_dob_str="1970-05-01"
    )
    print(compatibility_output)

    # Example: LP 3 and LP 3
    compatibility_output_2 = generate_life_path_compatibility_output(
        person1_name="Creative Three A", person1_dob_str="1970-02-02", # LP3
        person2_name="Creative Three B", person2_dob_str="1973-02-02"  # LP3 (2+0+1+9+7+3 = 22 => 4, no, 1+9+7+3+0+2+0+2 = 24 => 6)
                                                                      # Let's use another LP3: 1980-02-02 -> 1+9+8+0+0+2+0+2 = 22 -> 4
                                                                      # For LP3: 1972-01-01 -> 1+9+7+2+0+1+0+1 = 21 -> 3
    )
    print(compatibility_output_2)
    
    # Test for a pair that might be ordered differently (e.g. 5 and 1)
    compatibility_output_3 = generate_life_path_compatibility_output(
        person1_name="Adventurer Five", person1_dob_str="1970-05-01", # LP5
        person2_name="Pioneer One", person2_dob_str="1970-01-01"    # LP1
    )
    print(compatibility_output_3)


    print("\n--- Script Execution Finished ---")