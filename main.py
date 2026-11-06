
from pyscript import document

# Dictionary containing the information of non-metal elements.
# Each symbol is a key, while its tuple stores the name,
# atomic number, and atomic mass, respectively.

non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "SE": ("Selenium", 34, 78.971),
    "HE": ("Helium", 2, 4.0026),
    "NE": ("Neon", 10, 20.180),
    "AR": ("Argon", 18, 39.948),
    "KR": ("Krypton", 36, 83.798),
    "XE": ("Xenon", 54, 131.293),
    "RN": ("Radon", 86, 222),
    "F": ("Fluorine", 9, 18.998),
    "CL": ("Chlorine", 17, 35.45),
    "BR": ("Bromine", 35, 79.904),
    "I": ("Iodine", 53, 126.904),
    "AT": ("Astatine", 85, 210),
    "TS": ("Tennessine", 117, 294)
}


# Function that searches for an element using its entered symbol.
def search_element(event):

    # Retrieves the user's input from the HTML text field.
    # Converts the input to uppercase and removes extra spaces.
    Element1 = document.getElementById("Element1").value.upper().strip()

    # Searches the dictionary for the entered element symbol.
    # Returns a default tuple if the symbol is not in the dictionary.
    result = non_metals.get(
        Element1,
        ("Element not found", "-", "-")
    )

    # Extracts the element's details from their respective tuple positions.
    element_name = result[0]
    atomic_number = result[1]
    atomic_mass = result[2]

    # Displays the entered symbol in the corresponding HTML result field.
    document.getElementById("symbol_result").innerText = Element1

    # Displays the element's complete name retrieved from the dictionary.
    document.getElementById("name_result").innerText = element_name

    # Displays the element's atomic number.
    document.getElementById("number_result").innerText = atomic_number

    # Displays the element's atomic mass.
    document.getElementById("mass_result").innerText = atomic_mass
