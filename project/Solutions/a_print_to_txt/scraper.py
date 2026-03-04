import requests
from pathlib import Path

from bs4 import BeautifulSoup


URL = "https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations"
HEADERS = {"User-Agent": "<Your name here>"}


def scrape_countries() -> list[str]:
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", class_="wikitable")
    if table is None:
        raise RuntimeError("Could not find countries table on the page")

    countries: list[str] = []

    for row in table.find_all("tr")[1:]:  # Skip header row
        country_cell = row.th

        link = country_cell.a
        name = link.text
        countries.append(name)

    return sorted(countries)


def save_countries(countries: list[str]) -> None:
    with open("countries.txt", "w") as file:
        file.write("\n".join(countries))


if __name__ == "__main__":
    countries_list = scrape_countries()
    save_countries(countries_list)
    print(f"Saved {len(countries_list)} countries to countries.txt")
