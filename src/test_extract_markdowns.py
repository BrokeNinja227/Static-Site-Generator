import unittest
from src.extract_markdowns import *

class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://github.com/BrokeNinja227/Static-Site-Generator)"
        )
        self.assertListEqual([("link", "https://github.com/BrokeNinja227/Static-Site-Generator")], matches)

    def test_no_text_links(self):
        with self.assertRaisesRegex(Exception, "text field cannot be empty"):
            extract_markdown_links("")

    def test_no_text_images(self):
        with self.assertRaisesRegex(Exception, "text field cannot be empty"):
            extract_markdown_images("")

    def test_no_links_in_text(self):
        matches = extract_markdown_links("This is text with no link")
        self.assertListEqual([], matches)

    def test_no_images_in_text(self):
        matches = extract_markdown_images("This is text with no image")
        self.assertListEqual([], matches)

if __name__ == "__main__":
    unittest.main()
