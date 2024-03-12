from bs4 import BeautifulSoup
import requests
import os
import json
# Read in file with a filename and return links 
def read_file():            
    try:
        filename = input("Enter the filename: ")
        # Set up input folder and process
        input_folder = "Data/unprocessed"
        new_filename = os.path.join(input_folder, filename)
        with open(new_filename, 'r') as file:
            article_links = [line.strip() for line in file.readlines()]
            return article_links
    except FileNotFoundError:
        print(f"File {new_filename} not found")
