import unittest
from src.blocktype import *

class TestBlockType(unittest.TestCase):

    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        self.assertEqual(BlockType.HEADING, BlockType.block_to_block_type(block))

    def test_block_to_block_type_code(self):
        block = "```\ndef example_function():\n    return 'Hello world'\n```"
        self.assertEqual(BlockType.CODE, BlockType.block_to_block_type(block))

    def test_block_to_block_type_quote(self):
        block = ">This is a quote\n>This is the second line of the quote"
        self.assertEqual(BlockType.QUOTE, BlockType.block_to_block_type(block))

    def test_block_to_block_type_unordered_list(self):
        block = "- First item\n- Second item\n- Third item"
        self.assertEqual(BlockType.UNORDERED_LIST, BlockType.block_to_block_type(block))

    def test_block_to_block_type_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(BlockType.ORDERED_LIST, BlockType.block_to_block_type(block))

    def test_block_to_block_type_heading_2(self):
        block = "### This is a level 3 heading"
        self.assertEqual(BlockType.HEADING, BlockType.block_to_block_type(block))
