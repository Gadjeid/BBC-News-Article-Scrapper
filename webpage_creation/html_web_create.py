import os
from xml.etree import ElementTree as ET

articles_path = "Data/processed/summaries"
articles_agg = "webpage_creation/articles_input.txt"
html_file = "webpage_creation/articles.html"

def aggregate_articles():
    try:
        with open(articles_agg, "w") as output_file:
                # Iterate through list with article summaries in Data/processed/summaries if it ends in .txt
            print("articles_path", articles_path)
            for index, file_name in enumerate(os.listdir(articles_path), start=1):
                if file_name.endswith('.txt'):
                    # Set up input file
                    summary_file = os.path.join(articles_path, file_name)

                    with open(summary_file, "r") as input:
                        lines = input.readlines()
                        title = None
                        content = ""

                        # Process each line
                        for line in lines:
                            if line.startswith("Headline: "):
                                title = line[len("Headline: "):].strip()
                            else:
                                content += line
                        output_file.write(f"{title}\n")
                        output_file.write(f"{content}\n")
    except FileNotFoundError:
        print("Error: directory does not exist")

def txt_to_html():
    aggregate_articles()
    # Creare root for HTML
    root = ET.Element("html")

    # Create head and body elements
    head = ET.SubElement(root, "head")
    title = ET.SubElement(head, "title")
    title.text = "My News Aggregation Site - Godfred Adjei-Darko"
    body = ET.SubElement(root, "body")

    style = ET.SubElement(head, "style")
    style.text = "body { background-color: black; color : white;}"

    with open(articles_agg, 'r') as f:
        content = f.readlines()

    for i in range(0, len(content), 2):
        # Extract header and paragraph for article
        header = content[i].strip()
        paragraph = content[i + 1].strip()

        # Header and paragraph elements
        h1 = ET.SubElement(body, "h1")
        h1.text = header
        p = ET.SubElement(body, "p")
        p.text = paragraph
    
    with open(html_file, 'wb') as f:
        tree = ET.ElementTree(root)
        tree.write(f, encoding='utf-8')
