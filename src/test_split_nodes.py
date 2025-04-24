import unittest
from src.split_nodes import *
from src.textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_with_delimiter(self):
        node = TextNode("This is text with a `code block` example", TextType.TEXT)
        expected_output = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" example", TextType.TEXT)
        ]
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, expected_output)

    def test_split_with_delimiter_missing_from_text(self):
        node = TextNode("This is text with no delimiter", TextType.TEXT)
        expected_output = [
            TextNode("This is text with no delimiter", TextType.TEXT),
        ]
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, expected_output)

    def test_unmatched_delimiter_raises_exception(self):
        node = TextNode("Text `with an `unmatched` delimiter", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertTrue("unmatched delimiter in text" in str(context.exception))

    def test_split_with_delimiter_at_start_of_text(self):
        node = TextNode("`This is text with a code block` example", TextType.TEXT)
        expected_output = [
            TextNode("This is text with a code block", TextType.CODE),
            TextNode(" example", TextType.TEXT)
        ]
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, expected_output)

    def test_with_more_than_three_delimiters(self):
        node = TextNode("This `is` text `with` a `code block` example", TextType.TEXT)
        expected_output = [
            TextNode("This ", TextType.TEXT),
            TextNode("is", TextType.CODE),
            TextNode(" text ", TextType.TEXT),
            TextNode("with", TextType.CODE),
            TextNode(" a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" example", TextType.TEXT)
        ]
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, expected_output)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da) and another [second link](https://github.com/BrokeNinja227/Static-Site-Generator)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://github.com/BrokeNinja227/Static-Site-Generator"
                ),
            ],
            new_nodes,
        )

    def test_mixed_content(self):
        node = TextNode(
            "This is text with a ![image](https://image.png) and a [link](https://link.com) mixed together",
            TextType.TEXT,
        )
        image_nodes = split_nodes_image([node])
        mixed_nodes = split_nodes_link(image_nodes)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://image.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.com"),
                TextNode(" mixed together", TextType.TEXT),
            ],
            mixed_nodes,
        )

    def test_empty_node(self):
        node = TextNode("", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_link([node])
        self.assertTrue("text field cannot be empty" in str(context.exception))

    def test_with_no_link(self):
        original_node = TextNode("This is just plain text with no links", TextType.TEXT)
        result = split_nodes_link([original_node])
        self.assertListEqual([original_node], result)

    def test_with_link_at_beginning(self):
        node = TextNode("[link](https://link.com) is at the beginning of the text", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://link.com"),
                TextNode(" is at the beginning of the text", TextType.TEXT),
            ],
            result,
        )
