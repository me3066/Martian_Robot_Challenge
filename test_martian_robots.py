import io
import sys
import unittest
from martian_robots import main

def run_program(input_text):
    """Run the main program with given input text and return its output."""
    sys.stdin = io.StringIO(input_text)
    sys.stdout = io.StringIO()
    main()
    return sys.stdout.getvalue().strip()


class MartianRobotsTests(unittest.TestCase):

    def test_sample_case(self):
        data = """\
5 3
1 1 E
RFRFRFRF

3 2 N
FRRFLLFFRRFLL

0 3 W
LLFFFLFLFL
"""
        expected = "1 1 E\n3 3 N LOST\n2 3 S"
        self.assertEqual(run_program(data), expected)

    def test_lost_on_first_move(self):
        data = """\
1 1
1 1 N
F
"""
        expected = "1 1 N LOST"
        self.assertEqual(run_program(data), expected)

    def test_no_commands(self):
        data = """\
2 2
0 0 N

"""
        expected = "0 0 N"
        self.assertEqual(run_program(data), expected)

    def test_ignore_scented_edge(self):
        data = """\
1 1
1 1 N
F
1 1 N
F
"""
        expected = "1 1 N LOST\n1 1 N"
        self.assertEqual(run_program(data), expected)


if __name__ == "__main__":
    unittest.main()
