import pytest

from wordsearch_generator.main import GridGenerator, WordDoesNotFitException

def test_generate_grid():
    # Given
    generator = GridGenerator()
    width = 5
    length = 3

    # When
    grid = generator.generate_grid(width, length)

    # Then
    assert isinstance(grid, list)
    assert len(grid) == length
    assert all(isinstance(row, list) and len(row) == width for row in grid)

def test_insert_word_in_grid():
    # Given
    generator = GridGenerator()
    width = 5
    length = 3
    word = "hello"

    # When
    grid = generator.generate_grid(width, length)
    generator.insert_word_in_grid_horizontally(word, grid)

    # Then
    # Check if the word is inserted correctly in the grid
    for i, char in enumerate(word):
        assert grid[0][i] == char

    # Check if the rest of the grid cells are empty
    for row in grid:
        for cell in row[len(word):]:
            assert cell == ''

def test_insert_word_in_grid_raises_exception():
    # Given
    generator = GridGenerator()
    width = 3
    length = 3
    word = "hello"

    # When
    grid = generator.generate_grid(width, length)

    # Then
    with pytest.raises(WordDoesNotFitException):
        generator.insert_word_in_grid_horizontally(word, grid)

def test_insert_word_in_grid_vertically():
    # Given
    generator = GridGenerator()
    width = 3
    length = 5
    word = "hello"

    # When
    grid = generator.generate_grid(width, length)
    generator.insert_word_in_grid_vertically(word, grid)

    # Then
    # Check if the word is inserted correctly in the grid
    for i, char in enumerate(word):
        assert grid[i][0] == char

    # Check if the rest of the grid cells are empty
    for col in range(1, width):
        for row in grid:
            assert row[col] == ''

def test_insert_word_in_grid_diagonally():
    # Given
    generator = GridGenerator()
    width = 5
    length = 5
    word = "hello"

    # When
    grid = generator.generate_grid(width, length)
    generator.insert_word_in_grid_diagonally(word, grid)

    # Then
    # Check if the word is inserted correctly in the grid
    for i, char in enumerate(word):
        assert grid[i][i] == char

    # Check if the rest of the grid cells are empty
    for i in range(len(word)):
        for j in range(len(word), width):
            assert grid[i][j] == ''
        for j in range(len(word), length):
            assert grid[j][i] == ''
