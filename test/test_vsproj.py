import unittest
from lib import vsproj


class TestUpdateVersionRevision(unittest.TestCase):
    def test_empty_version(self):
        version_text = vsproj.update_version_revision('')
        self.assertEqual('0.1.0.0', version_text)

    def test_version_without_postfix(self):
        version_text = vsproj.update_version_revision('3.2.4.6')
        self.assertEqual('3.2.4.7', version_text)

    def test_version_with_postfix(self):
        version_text = vsproj.update_version_revision('3.2.4.6-preview-1')
        self.assertEqual('3.2.4.7-preview-1', version_text)


if __name__ == "__main__":
    # import sys
    # sys.argv = ['', 'TestHello.testHello3']       # arguments, or input arguments from command line: filename.py TestHello.testHello3
    unittest.main()
