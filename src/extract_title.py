def extract_title(markdown):
    title = ""
    for line in markdown.split('\n'):
        if line.startswith('# '):
            title = line.strip('# ')
    if title == "":
        raise Exception("No h1 header in markdown")
    return title
