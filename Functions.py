import unittest


class TestStringMethods(unittest.TestCase):
    def move_north (direction):
        if direction == 'L':
            return 'W'
        return 'E'

    def calculate_position(self):
        size = ['5', '5']
        position = [1, 2, 'N']
        movement = ['L', 'M', 'L', 'M', 'L', 'M', 'L', 'M', 'M']

        for i in range(0, len(movement)):
            if movement[i] == 'L':
                if position[2] == 'N':
                    position[2] == 'W'



    def test_upper(self):

        self.assertEqual(move_north('L'), 'W')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()