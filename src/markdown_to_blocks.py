def markdown_to_blocks(markdown):
    # Split the markdown into blocks
    items = markdown.split("\n\n")
    blocks = []
    
    for item in items:
        # Remove leading/trailing whitespace from the entire block
        stripped = item.strip()
        if stripped:  # Skip empty blocks
            # Normalize internal newlines - split by newline, strip each line, rejoin
            lines = [line.strip() for line in stripped.split("\n")]
            normalized_block = "\n".join(lines)
            blocks.append(normalized_block)
    
    return blocks
