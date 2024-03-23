import unittest
from analysis import analyze_demographics

class TestAnalyzeDemographics(unittest.TestCase):
    def test_basic_demographics(self):
        """
        Test analyze_demographics with basic, correctly structured input.
        """
        artist_demographics = {
            'Artist1': {
                'gender': {'person1': 'female', 'person2': 'male'},
                'age': {'person1': 25, 'person2': 30},
                'location': {'person1': 'United States', 'person2': 'Canada'}
            }
        }
        expected = {
            'gender': {'male': 1, 'female': 1, 'other': 0},
            'average_age': 27.5,
            'location': {'United States': 1, 'Canada': 1}
        }
        result = analyze_demographics(artist_demographics)
        self.assertEqual(result, expected)

    def test_missing_keys(self):
        """
        Test analyze_demographics with missing keys in input.
        """
        artist_demographics = {
            'Artist2': {}  # Missing 'gender', 'age', 'location' keys
        }
        expected = {
            'gender': {'male': 0, 'female': 0, 'other': 0},
            'average_age': 0,
            'location': {}
        }
        result = analyze_demographics(artist_demographics)
        self.assertEqual(result, expected)

    def test_incorrect_structure(self):
        """
        Test analyze_demographics with incorrect data structure (lists instead of dicts).
        """
        artist_demographics = {
            'Artist3': {
                'gender': ['male', 'female'],  # Incorrect structure
                'age': [25, 30],  # Incorrect structure
                'location': ['United States', 'Canada']  # Incorrect structure
            }
        }
        expected = {
            'gender': {'male': 0, 'female': 0, 'other': 0},
            'average_age': 0,
            'location': {}
        }
        result = analyze_demographics(artist_demographics)
        self.assertEqual(result, expected)

    def test_incorrect_structure(self):
        """
        Test `analyze_demographics` with various incorrect data structures.
        """
        artist_demographics = {
            'Artist1': {
                'gender': ['male', 'female'],  # Incorrect structure
                'age': {'person1': 30},  # Correct structure
                'location': 'United States'  # Missing encapsulating dict
            },
            'Artist2': {
                # Missing gender
                'age': {'person2': 40},
                'location': {'person2': 'Canada'}  # Correct structure
            }
        }

        expected_result = {
            'gender': {'male': 1, 'female': 1, 'other': 0},  # Assuming 'male' and 'female' counted once each
            'average_age': 35,
            'location': {'United States': 1, 'Canada': 1}
        }
        
        result = analyze_demographics(artist_demographics)
        self.assertEqual(result, expected_result)

# If this script is run directly, run the tests
if __name__ == '__main__':
    unittest.main()
