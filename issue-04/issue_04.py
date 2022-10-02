from one_hot_encoder import fit_transform
import pytest


def test_cities():
    """Testing cities list."""
    actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_pokemons():
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
    assert actual == expected


def test_empty_list():
    """Testing empty list."""
    actual = fit_transform([])
    expected = []
    assert actual == expected


def test_empty_str():
    """Testing list with empty string."""
    actual = fit_transform([''])
    expected = [('', [1])]
    assert actual == expected


def test_empty_input():
    """Testing exception raising with empty input."""
    with pytest.raises(TypeError):
        fit_transform()


def test_lists_input():
    """Testing exception raising with wrong input."""
    with pytest.raises(TypeError):
        fit_transform([['1'], ['2']])


def test_range_input_to_list_transform():
    """Testing transforming of iterator to list."""
    assert isinstance(fit_transform(range(1, 10)), list)


def test_dicts_input():
    """Testing transforming of few dicts at input."""
    assert '3' not in fit_transform(
        {'1': 'text_1', '2': 'text_2'},
        {'3': 'text_3'}
    )


if __name__ == "__main__":
    pytest.main()
