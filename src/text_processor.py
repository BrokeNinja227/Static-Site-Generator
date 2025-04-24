from src.textnode import TextNode, TextType
from src.split_nodes import *

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    bold = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    italic = split_nodes_delimiter(bold, '_', TextType.ITALIC)
    code = split_nodes_delimiter(italic, '`', TextType.CODE)
    images = split_nodes_image(code)
    links = split_nodes_link(images)
    return links
