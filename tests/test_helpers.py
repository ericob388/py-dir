import io
import sys
import unittest
from helpers import iohelper


class TestIOHelper(unittest.TestCase):

    def test_help_print(self):
        # Redirect stdout
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        iohelper.help_print('test')
        self.assertEqual('test\n', capturedOutput.getvalue())

        # Reset redirect.
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
