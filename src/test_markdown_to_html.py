import unittest
from src.markdown_to_html import *

class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """
### This is text that _should_ be italic the **bold** text should be bold
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><h3>This is text that <i>should</i> be italic the <b>bold</b> text should be bold</h3></div>",
        )

    def test_unordered_list(self):
        md = """
- This
- is
- an
- unordered
- list
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><ul><li>This</li><li>is</li><li>an</li><li>unordered</li><li>list</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
1. This
2. is
3. an
4. ordered
5. list
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><ol><li>This</li><li>is</li><li>an</li><li>ordered</li><li>list</li></ol></div>"
        )

    def test_blockquote(self):
        md = """
>This text is a quote.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><blockquote>This text is a quote.</blockquote></div>"
        )

