import unittest
from src.extract_title import extract_title

class TestBlockType(unittest.TestCase):

    def test_extract_title(self):
        md = """
# This is an h1 Title\n
This is another line that is not part of the title.\n
This is yet another line
"""
        self.assertEqual("This is an h1 Title", extract_title(md))

    def test_extract_title_2(self):
        md = """
This is a line that is not part of the title.\n
# This is an h1 Title\n
This is yet another line
"""
        self.assertEqual("This is an h1 Title", extract_title(md))

    def test_extract_title_3(self):
        md = """
## This is an h2 Title\n
This is another line that is not part of the title.\n
This is yet another line 
"""
        with self.assertRaisesRegex(Exception, "No h1 header in markdown"):
            extract_title(md)
