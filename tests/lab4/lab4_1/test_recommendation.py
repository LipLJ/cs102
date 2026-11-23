import unittest
import tempfile
import os
from lab4.lab4_1.recommendation_service import RecommendationService


class TestRecommendationService(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.movies_file = os.path.join(
            self.temp_dir.name, "../../../src/lab4/lab4_1/movies.txt"
        )
        self.history_file = os.path.join(
            self.temp_dir.name, "../../../src/lab4/lab4_1/history.txt"
        )
        with open(self.movies_file, "w", encoding="utf-8") as file:
            file.write(
                "1,Фильм 1\n"
                "2,Фильм 2\n"
                "3,Фильм 3\n"
                "4,Фильм 4\n"
            )
        with open(self.history_file, "w", encoding="utf-8") as file:
            file.write(
                "1,2,3\n"
                "1,2,4,4\n"
            )
        self.service = RecommendationService(
            self.movies_file,
            self.history_file
            )
    def tearDown(self):
        self.temp_dir.cleanup()
    def test_recommendation(self):
        result = self.service.recommend([1, 2, 3])
        self.assertIsNotNone(result)
        self.assertEqual(result.title, "Фильм 4")
    def test_empty_history(self):
        result = self.service.recommend([])
        self.assertIsNone(result)
    def test_no_recommendation(self):
        result = self.service.recommend([1, 2, 3, 4])
        self.assertIsNone(result)
    def test_watched_movie_not_recommended(self):
        result = self.service.recommend([1, 2, 3])
        if result:
            self.assertNotIn(result.movie_id, [1, 2, 3])
if __name__ == "__main__":
    unittest.main()