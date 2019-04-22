import unittest
import filecmp
import sys
from io import StringIO
import robot_navigation
from robot_navigation import *


class TestStringMethods(unittest.TestCase):
    # tests all the functions that are responsible for returning states (E, W, N, S)
    def test_state(self):
        func_list = [west(), east(), north(), south()]
        result_list = ['W', 'E', 'N', 'S']
        for i in range(0, len(func_list)):
            self.assertEqual(func_list[i], result_list[i])

    # tests all the functions that are responsible to run checks for L, M, states
    def test_checks(self):
        func_list_true = [is_left('L'), is_move('M'), is_north('N'), is_west('W'), is_east('E'), is_south('S')]
        func_list_false = [is_left('R'), is_move('L'), is_north('S'), is_west('E'), is_east('W'), is_south('N')]
        for func in func_list_true:
            self.assertTrue(func)
        for func in func_list_false:
            self.assertFalse(func)

    # tests all the swap functions
    def test_swaps(self):
        func_list = [swap_north('W'), swap_north('E'), swap_east('N'), swap_east('S')]
        result_list = ['E', 'W', 'S', 'N']
        for i in range(0, len(func_list)):
            self.assertEqual(func_list[i], result_list[i])

    # tests all the change functions
    def test_change(self):
        func_list = [change_north('L'), change_north('R'), change_south('L'), change_south('R'), change_east('L'), change_east('R'), change_west('L'), change_west('R')]
        result_list = ['W', 'E', 'E', 'W', 'N', 'S', 'S', 'N']
        for i in range(0, len(func_list)):
            self.assertEqual(func_list[i], result_list[i])

    # testing the move from a direction
    def test_move(self):
        self.assertEqual(move('N', 'L', is_north, change_north), 'W')

    # tests all the change states from a specific position
    def test_change(self):
        func_list = [from_north('N', 'L'), from_south('S', 'L'), from_east('E', 'L'), from_west('W', 'R')]
        result_list = ['W', 'E', 'N', 'N']
        for i in range(0, len(func_list)):
            self.assertEqual(func_list[i], result_list[i])

    # testing the functions to increase and decrease positions
    def test_inde(self):
        self.assertEqual(increase([1, 2, 'N'], 1, 5), 3)
        self.assertEqual(decrease([1, 0, 'N'], 1), 0)

    # testing the move from an axis, including sides and keep/change
    def test_side(self):
        self.assertTrue(which_side('N', is_north, is_south))
        self.assertEqual(keep([1, 2, 'N'], is_east, is_west, 0), 0)
        self.assertEqual(change([1, 2, 'N'], is_north, 1, 5), '3')

    # check the conversion to list
    def test_convert(self):
        self.assertEqual(convert('1 2 N'), [1, 2, 'N'])

    # test the function to derive result from an input
    def test_final_position(self):
        self.assertEqual(find_position([1, 2, 'N'], ['M', 'L', 'M'], [5, 2]), [0, 2, 'W'])

    # test the main function with an input and output file
    def test_main(self):
        # open a file to write output
        index = 4
        store_output = ""

        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        # take in the input file
        sys.stdin = open("inputs.txt")
        robot_navigation.main()
        sys.stdout = old_stdout
        result = mystdout.getvalue()
        list_result = result.split('\n')

        # write the results in a string
        while index < len(list_result):
            store_output += str(list_result[index])
            store_output += "\n"
            index = index + 3

        # write the results in an output file
        output = open("outputs.txt", "w+")
        output.write(store_output)
        output.close()

        self.assertTrue(filecmp.cmp('outputs.txt', 'expected_outputs.txt'))


if __name__ == '__main__':
    unittest.main()