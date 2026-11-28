
import unittest

from lab4.lab4_2.main import (
    Respondent,
    AgeGroup,
    SurveyGrouper
)


class TestAgeGroup(unittest.TestCase):

    def test_contains(self):
        group = AgeGroup(19, 25)

        self.assertTrue(group.contains(19))
        self.assertTrue(group.contains(25))
        self.assertFalse(group.contains(18))
        self.assertFalse(group.contains(26))

    def test_last_group(self):
        group = AgeGroup(101, None)

        self.assertTrue(group.contains(101))
        self.assertTrue(group.contains(123))
        self.assertFalse(group.contains(100))

    def test_label(self):
        group = AgeGroup(19, 25)
        self.assertEqual(group.get_label(), "19-25")

        last_group = AgeGroup(101, None)
        self.assertEqual(last_group.get_label(), "101+")


class TestSurveyGrouper(unittest.TestCase):

    def setUp(self):
        self.grouper = SurveyGrouper(
            [18, 25, 35, 45, 60, 80, 100]
        )

    def test_create_groups(self):
        self.assertEqual(len(self.grouper.groups), 8)
        self.assertEqual(
            self.grouper.groups[0].get_label(), "0-18"
        )
        self.assertEqual(
            self.grouper.groups[-1].get_label(), "101+"
        )

    def test_find_group(self):
        self.assertEqual(
            self.grouper.find_group(15).get_label(), "0-18"
        )
        self.assertEqual(
            self.grouper.find_group(25).get_label(), "19-25"
        )
        self.assertEqual(
            self.grouper.find_group(105).get_label(), "101+"
        )

    def test_group_respondents(self):
        respondents = [
            Respondent("Иванов Иван", 20),
            Respondent("Петров Петр", 15),
            Respondent("Сидоров Сидор", 30)
        ]

        result = self.grouper.group_respondents(respondents)

        self.assertEqual(len(result), 3)

    def test_sorting(self):
        respondents = [
            Respondent("Петров Петр", 20),
            Respondent("Сидоров Сидор", 25),
            Respondent("Иванов Иван", 25)
        ]

        result = self.grouper.group_respondents(respondents)
        self.grouper.sort_respondents(result)

        people = result[self.grouper.find_group(20)]

        self.assertEqual(
            [person.name for person in people],
            [
                "Иванов Иван",
                "Сидоров Сидор",
                "Петров Петр"
            ]
        )

    def test_empty_groups(self):
        respondents = [Respondent("Иванов Иван", 15)]

        result = self.grouper.process(respondents)

        self.assertNotIn("19-25:", result)
        self.assertIn("0-18:", result)

    def test_empty_respondents(self):
        result = self.grouper.process([])
        self.assertEqual(result, "")

    def test_invalid_boundaries(self):
        with self.assertRaises(ValueError):
            SurveyGrouper([])

        with self.assertRaises(ValueError):
            SurveyGrouper([18, 25, 20])

        with self.assertRaises(ValueError):
            SurveyGrouper([18, 18])

        with self.assertRaises(ValueError):
            SurveyGrouper([130])

        with self.assertRaises(ValueError):
            SurveyGrouper([-1])

    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            self.grouper.find_group(-1)

        with self.assertRaises(ValueError):
            self.grouper.find_group(124)


if __name__ == "__main__":
    unittest.main()
