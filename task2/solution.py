import csv
import re
import urllib.parse
from typing import Dict
from urllib.request import urlopen


WIKI_CATEGORY_URL = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

def fetch_wiki_page(url: str) -> str:
    encoded_url = urllib.parse.quote(url, safe=':/')
    with urlopen(encoded_url) as response:
        return response.read().decode("utf-8")

def extract_animals(html: str) -> list:
    pattern = r'<li><a href="/wiki/[^"]+" title="([^"]+)">'
    return re.findall(pattern, html)

def count_animals_by_letter(animals: list) -> Dict[str, int]:
    counts = {}
    for animal in animals:
        if not animal:
            continue
        first_char = animal[0].upper()
        if 'А' <= first_char <= 'Я':
            counts[first_char] = counts.get(first_char, 0) + 1
    return counts

def write_to_csv(data: dict, filename: str):
    with open(filename, "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        for letter, count in sorted(data.items()):
            writer.writerow([letter, count])

def main():
    html = fetch_wiki_page(WIKI_CATEGORY_URL)
    animals = extract_animals(html)
    counts = count_animals_by_letter(animals)
    write_to_csv(counts, "beasts.csv")
    print(f"Обработано {len(animals)} записей. Результат сохранён в beasts.csv")

if __name__ == "__main__":
    main()