
import unittest

from src.lab3.sudoku import (
    group,
    get_row,
    get_col,
    get_block,
    find_empty_positions,
    find_possible_values,
    solve,
    check_solution,
    generate_sudoku,
)


class TestSudoku(unittest.TestCase):

    def test_group(self):
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(group(list(range(1, 10)), 3),
                         [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_get_row(self):
        grid = [
            list("123456789"),
            list("abcdefghi"),
            list("........."),
            list("........."),
            list("........."),
            list("........."),
            list("........."),
            list("........."),
            list("........."),
        ]
        self.assertEqual(get_row(grid, (1, 0)), list("abcdefghi"))

    def test_get_col(self):
        grid = [list("123456789") for _ in range(9)]
        self.assertEqual(get_col(grid, (0, 2)), ["3"] * 9)

    def test_get_block(self):
        grid = [list("123456789") for _ in range(9)]
        self.assertEqual(
            get_block(grid, (0, 0)),
            list("123123123")
        )

    def test_find_empty_positions(self):
        grid = [list("123456789") for _ in range(9)]
        grid[2][4] = "."
        self.assertEqual(find_empty_positions(grid), (2, 4))

        full_grid = [list("123456789") for _ in range(9)]
        self.assertIsNone(find_empty_positions(full_grid))

    def test_find_possible_values(self):
        grid = [
            list("12345678."),
            list("........."),
            list("........."),
            list("........."),
            list("........."),
            list("........."),
            list("........."),
            list("........."),
            list("........."),
        ]
        self.assertEqual(find_possible_values(grid, (0, 8)), {"9"})

    def test_solve(self):
        grid = [
            list("53467891."),
            list("672195348"),
            list("198342567"),
            list("859761423"),
            list("426853791"),
            list("713924856"),
            list("961537284"),
            list("287419635"),
            list("345286179"),
        ]
        solution = solve(grid)
        self.assertIsNotNone(solution)
        self.assertTrue(check_solution(solution))

    def test_check_solution(self):
        solution = [
            list("534678912"),
            list("672195348"),
            list("198342567"),
            list("859761423"),
            list("426853791"),
            list("713924856"),
            list("961537284"),
            list("287419635"),
            list("345286179"),
        ]
        self.assertTrue(check_solution(solution))

        invalid_solution = [row.copy() for row in solution]
        invalid_solution[0][0] = "1"
        self.assertFalse(check_solution(invalid_solution))

    def test_generate_sudoku(self):
        grid = generate_sudoku(40)
        self.assertEqual(
            sum(1 for row in grid for cell in row if cell == "."),
            41,
        )

        grid = generate_sudoku(1000)
        self.assertEqual(
            sum(1 for row in grid for cell in row if cell == "."),
            0,
        )

        grid = generate_sudoku(0)
        self.assertEqual(
            sum(1 for row in grid for cell in row if cell == "."),
            81,
        )


if __name__ == "__main__":
    unittest.main()
