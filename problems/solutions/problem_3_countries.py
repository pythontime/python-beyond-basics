"""Create text files for each letter that contain
all the countries that start with that letter
"""
from pathlib import Path
from pprint import pprint
from collections import defaultdict

countries_path = Path(__file__).parent / "data" / "countries.txt"

with open(countries_path, "r") as file:
    country_letter_map = defaultdict(list)
    for country in file.readlines():
        country_letter_map[country[0]].append(country.strip())

pprint(country_letter_map)

for letter, countries in country_letter_map.items():
    with open(countries_path.parent / f"{letter}_countries.txt", "w") as file:
        file.write("\n".join(countries))
