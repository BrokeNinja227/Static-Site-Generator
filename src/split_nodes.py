from src.textnode import TextNode, TextType
from src.extract_markdowns import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if delimiter == "":
        raise ValueError("delimiter cannot be an empty string")
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid Markdown syntax: unmatched delimiter in text: " + node.text)
        text_list = node.text.split(delimiter)
        is_special = False 
        for segment in text_list:
            if segment:
                current_type = text_type if is_special else TextType.TEXT
                new_nodes.append(TextNode(segment, current_type))
            is_special = not is_special
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            parts = remaining_text.split(image_markdown, 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for anchor_text, url in links:
            link_markdown = f"[{anchor_text}]({url})"
            parts = remaining_text.split(link_markdown, 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes
