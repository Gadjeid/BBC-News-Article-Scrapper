from bs4 import BeautifulSoup
import requests
import os
import json
# Read in file with a filename and return links 
def read_file():            
    try:
        filename = input("Enter the filename: ")
        output_folder = "Data/unprocessed"
        new_filename = os.path.join(output_folder, filename)
        with open(new_filename, 'r') as file:
            article_links = [line.strip() for line in file.readlines()]
            return article_links
    except FileNotFoundError:
        print(f"File {new_filename} not found")
