import unittest

from task2.solution import (
    fetch_wiki_page,
    extract_animals,
    count_animals_by_letter,
    WIKI_CATEGORY_URL
)


class TestWikiAnimalCounterWithNetwork(unittest.TestCase):

    def test_fetch_wiki_page(self):
        html = fetch_wiki_page(WIKI_CATEGORY_URL)
        self.assertIn("<html", html.lower())

    def test_extract_animals(self):
        html = fetch_wiki_page(WIKI_CATEGORY_URL)
        animals = extract_animals(html)
        self.assertIsInstance(animals, list)
        self.assertGreater(len(animals), 0)
        for animal in animals:
            self.assertIsInstance(animal, str)

    def test_count_animals_by_letter(self):
        html = fetch_wiki_page(WIKI_CATEGORY_URL)
        animals = extract_animals(html)
        counts = count_animals_by_letter(animals)

        self.assertIsInstance(counts, dict)
        for letter, count in counts.items():
            self.assertTrue('А' <= letter <= 'Я', f"Недопустимая буква: {letter}")
            self.assertIsInstance(count, int)
            self.assertGreaterEqual(count, 0)


if __name__ == '__main__':
    unittest.main()