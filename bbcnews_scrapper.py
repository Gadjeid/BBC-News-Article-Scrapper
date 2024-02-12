from bs4 import BeautifulSoup
import requests
import json
# Read in file with article links and return
def read_file():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            article_links = [line.strip() for line in file.readlines()]
            return article_links
    except FileNotFoundError:
        print(f"File {filename} not found")

def soup_scrap(article_links):
    for index, link in enumerate(article_links, 0):
        # Make a request to each article link
        response = requests.get(link)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Take reponse and parse
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find the h1 (title) and all paragraphs (summary & article)
            headline = soup.find('h1')
            article = soup.find_all('p', class_="sc-eb7bd5f6-0 fYAfXe")
            tags = soup.find_all(class_="sc-3df0d64d-0 kMyFYO")

            # Remmove unnecessary social media promotion
            for p_tag in soup.find_all('p', class_='sc-7dcfb11b-0 kKcaog'):
                p_tag.decompose()
            
            # Print all for each article (headline, summary, article)
            output_filename = f"article_{index+1}.txt"
            # Read outputs to file
            with open(output_filename, 'w') as output_file:
                output_file.write("Headline: " + headline.text.strip() + "\n" )
                output_file.write("Summary: " + article[0].text.strip() + "\n")

                content=""
                for a in article:
                    if a.text.strip() != article[0].text.strip():
                        content+= str(a.text.strip()) + " "
                output_file.write("Article: " + content + "\n")

                article_tag=""
                for i, tag in enumerate(tags):
                # Print the tag without a newline
                    article_tag+=str(tag.text.strip())
                # Add a comma if it's not the last tag
                    if i < len(tags) - 1:
                        article_tag+=", "
                output_file.write("Tags: " + article_tag + "\n")
            print(f"article {index+1} scrapped, output in {output_filename}")
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")

def main():
    article_links = read_file()
    if article_links:
        soup_scrap(article_links)
    else:
        print("No article links found.")

if __name__ == "__main__":
    main()
