import unittest
from src import search

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.searchResults = search.searchFeedback("test")

    def test_search_results_type(self):
        self.assertIsInstance(self.searchResults, list)

    def test_search_results_content(self):
        for result in self.searchResults:
            self.assertIsInstance(result, dict)
            self.assertIn('project', result)
            self.assertIn('time', result)
            self.assertIn('feedback', result)

    def test_search_no_results(self):
        noResults = search.searchFeedback("nonexistent")
        self.assertEqual(noResults, [])

if __name__ == '__main__':
    unittest.main()