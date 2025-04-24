from src.markdown_to_blocks import markdown_to_blocks
from src.htmlnode import *
from src.blocktype import BlockType
from src.textnode import TextNode, TextType
from src.split_nodes import split_nodes_delimiter

def create_heading_level_and_text(block):
    if block.startswith('#'):
        tag = 'h1'
        text = block[1:].lstrip()
    if block.startswith('##'):
        tag = 'h2'
        text = block[2:].lstrip()
    if block.startswith('###'):
        tag = 'h3'
        text = block[3:].lstrip()
    if block.startswith('####'):
        tag = 'h4'
        text = block[4:].lstrip()
    if block.startswith('#####'):
        tag = 'h5'
        text = block[5:].lstrip()
    if block.startswith('######'):
        tag = 'h6'
        text = block[6:].lstrip()
    return tag, text

def text_to_children(text):
    text_nodes = [TextNode(text, TextType.TEXT)]
    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    html_nodes = []
    for text_node in text_nodes:
        html_node = TextNode.text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes

def handle_list_block(block, is_ordered=False):
    parent_tag = "ol" if is_ordered else "ul"
    items = []
    for line in block.split("\n"):
        line = line.strip()
        if line:
            if is_ordered:
                item_text = line[line.find(".")+1:].strip()
            else:
                item_text = line[2:].strip()
            items.append(item_text)
    li_nodes = []
    for item_text in items:
        children = text_to_children(item_text)
        li_node = HTMLNode(tag="li", children=children)
        li_nodes.append(li_node)
    return HTMLNode(tag=parent_tag, children=li_nodes)

def extract_quote_text(block):
    lines = block.split('\n')
    quote_lines = []
    for line in lines:
        if line.startswith(">"):
            line = line[1:]
            if line and line[0] == " ":
                line = line[1:]
        quote_lines.append(line)
    return "\n".join(quote_lines)

def extract_code_content(block):
    lines = block.split('\n')
    if lines[0].strip() == "```" and lines[-1].strip() == "```":
        content_lines = lines[1:-1]
        return "\n".join(content_lines) + "\n"
    else:
        if lines[0].strip() == "```":
            return "\n".join(lines[1:]) + "\n"
        raise Exception("code block fromatting error") 

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = BlockType.block_to_block_type(block)
        if block_type == BlockType.QUOTE:
            quote_text = extract_quote_text(block)
            children = text_to_children(quote_text)
            block_node = HTMLNode(tag="blockquote", children=children)
        elif block_type == BlockType.HEADING:
            tag, text = create_heading_level_and_text(block)
            children = text_to_children(text)
            block_node = HTMLNode(tag=tag, children=children)
        elif block_type == BlockType.CODE:
            code_content = extract_code_content(block)
            text_node = TextNode(code_content, TextType.TEXT)
            text_html_node = TextNode.text_node_to_html_node(text_node)
            code_node = HTMLNode(tag="code", children=[text_html_node])
            block_node = HTMLNode(tag="pre", children=[code_node])
        elif block_type == BlockType.UNORDERED_LIST:
            block_node = handle_list_block(block, is_ordered=False)
        elif block_type == BlockType.ORDERED_LIST:
            block_node = handle_list_block(block, is_ordered=True)
        elif block_type == BlockType.PARAGRAPH:
            block_text = block.replace("\n", " ")
            children = text_to_children(block_text)
            block_node = HTMLNode(tag='p', children=children)
        else:
            raise Exception("Test Error")
        block_nodes.append(block_node)
    parent_node = HTMLNode(tag="div", children=block_nodes)
    return parent_node
