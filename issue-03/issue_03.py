from one_hot_encoder import fit_transform
import unittest


class TestOHEncoder(unittest.TestCase):
    """Test class for unittest"""
    def test_cities(self):
        """Testing cities list."""
        actual = fit_transform(
            ['Moscow', 'New York', 'Moscow', 'London']
        )
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_pokemons(self):
        """Testing pokemons list with string multiplication."""
        actual = fit_transform(['Bulbasaur' * 2, 'Pikachu', 'Squirtle'] * 3)
        expected = [
            ('BulbasaurBulbasaur', [0, 0, 1]),
            ('Pikachu', [0, 1, 0]),
            ('Squirtle', [1, 0, 0]),
            ('BulbasaurBulbasaur', [0, 0, 1]),
            ('Pikachu', [0, 1, 0]),
            ('Squirtle', [1, 0, 0]),
            ('BulbasaurBulbasaur', [0, 0, 1]),
            ('Pikachu', [0, 1, 0]),
            ('Squirtle', [1, 0, 0])
        ]
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        """Testing empty list."""
        actual = fit_transform([])
        expected = []
        self.assertEqual(actual, expected)

    def test_empty_str(self):
        """Testing list with empty string."""
        actual = fit_transform([''])
        expected = [('', [1])]
        self.assertEqual(actual, expected)

    def test_empty_input(self):
        """Testing exception raising with empty input."""
        self.assertRaises(TypeError, fit_transform)

    def test_lists_input(self):
        """Testing exception raising with wrong input."""
        self.assertRaises(TypeError, fit_transform, [['1'], ['2']])

    def test_range_input_to_list_transform(self):
        """Testing transforming of iterator to list."""
        self.assertIsInstance(fit_transform(range(1, 10)), list)

    def test_dicts_input(self):
        """Testing transforming of few dicts at input."""
        self.assertNotIn('3',
                         fit_transform({'1': 'text_1', '2': 'text_2'},
                                       {'3': 'text_3'})
                         )


if __name__ == "__main__":
    unittest.main()
