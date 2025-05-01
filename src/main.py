import sys
print(sys.path)
from src.textnode import TextNode, TextType
import os
import shutil
from src.generate_page import generate_page, generate_pages_recursive
if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = '/'

def copy_and_move_contents(source_path, destination_path):
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)
    for item in os.listdir(source_path):
        item_path = os.path.join(source_path, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, destination_path)
            print(f"Copied file from {item_path} to {destination_path}")
        if os.path.isdir(item_path):
            new_subdirectory = os.path.join(destination_path, item)
            os.mkdir(new_subdirectory)
            copy_and_move_contents(item_path, new_subdirectory)

def main():
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    os.makedirs("docs")
    if os.path.exists("static"):
        for item in os.listdir("static"):
            source = os.path.join("static", item)
            destination = os.path.join("docs", item)
            if os.path.isdir(source):
                shutil.copytree(source, destination)
            else:
                shutil.copy2(source, destination)
    generate_pages_recursive("content/", "template.html", "docs/", basepath)

if __name__ == "__main__":
    main()
    print("Generation complete!")
