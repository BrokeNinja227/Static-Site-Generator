import re

def extract_markdown_images(text):
    if text == "":
        raise Exception("text field cannot be empty")
    alt_text_and_url = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return alt_text_and_url

def extract_markdown_links(text):
    if text == "":
        raise Exception("text field cannot be empty")    
    anchor_text_and_url = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return anchor_text_and_url
