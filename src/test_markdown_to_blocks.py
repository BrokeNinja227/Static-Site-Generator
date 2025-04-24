import unittest
from src.markdown_to_blocks import *

class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_input(self):
        self.assertEqual(markdown_to_blocks(""), [])

    def test_single_block(self):
        self.assertEqual(markdown_to_blocks("Just one block"), ["Just one block"])

    def test_excessive_newlines(self):
        self.assertEqual(
            markdown_to_blocks("Block 1\n\n\n\n\nBlock 2"),
            ["Block 1", "Block 2"]
        )

    def test_blockquotes(self):
        md = """
    Here's a paragraph before the quote

    > This is a blockquote in Markdown.
    > It spans multiple lines.
    >
    > It even has multiple paragraphs.

    And here's a paragraph after the quote
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Here's a paragraph before the quote",
                "> This is a blockquote in Markdown.\n> It spans multiple lines.\n>\n> It even has multiple paragraphs.",
                "And here's a paragraph after the quote"
            ]
        )
