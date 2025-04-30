from src.extract_title import extract_title
from src.htmlnode import HTMLNode
from src.markdown_to_html import markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path):
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path, 'r')
    md = markdown_file.read()
    markdown_file.close()
    template_file = open(template_path, 'r')
    template = template_file.read()
    template_file.close()
    node = markdown_to_html_node(md)
    md_html = node.to_html()
    title = extract_title(md)
    first_replacement = template.replace("{{ Title }}", title)
    full_HTML_file = first_replacement.replace("{{ Content }}", md_html)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    with open(dest_path, 'w') as f:
        f.write(full_HTML_file)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        if os.path.isdir(entry_path):
            dest_subdir = os.path.join(dest_dir_path, entry)
            os.makedirs(dest_subdir, exist_ok=True)
            generate_pages_recursive(entry_path, template_path, dest_subdir)
        elif entry.endswith(".md"):
            html_filename = entry[:-3] + ".html"
            page_dest_path = os.path.join(dest_dir_path, html_filename)
            generate_page(entry_path, template_path, page_dest_path)
