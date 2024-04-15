# Import openai (to make use of the LLM) and supply an API key
import os
from openai import OpenAI
client = OpenAI(api_key="ADD API KEY HERE")

# For summary using open ai, prompt given and summary is returned
def summarize(article_text):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Summarize this text in approximately 50 words."},
        {"role": "user", "content": f"The content of the article: {article_text}"}
        ]
    )
    summary = completion.choices[0].message.content
    return summary

def summarize_articles():
    # Create output location if not already present
    output_folder = 'Data/processed/summaries'
    
    #Test case 6 - if statement for folder verification / creation
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    articles_path = 'Data/processed'
    # Iterate through list with articles in Data/processed if it ends in .txt
    for index, file_name in enumerate(os.listdir(articles_path), start=1):
        if file_name.endswith('.txt'):
            with open(os.path.join(articles_path, file_name), 'r') as file:
                lines = file.readlines()
                title = None
                content = ""
                #Test case 7 - if-else statement for headline verification
                for line in lines:
                    # Save headline for output
                    if line.startswith("Headline: "):
                        title = line[len("Headline: "):].strip()
                    else:
                        content += line
                if title is not None:
                    # Summarize if title is found and output title and summary to .txt file in output folder
                    summary = summarize(content)

                    summary_file_path = os.path.join(output_folder, f'article_{index}_summary.txt')
                    with open(summary_file_path, 'w') as summary_file:
                        summary_file.write(f"Headline: {title}\n")
                        summary_file.write(summary)
                        # Test case 8: Output file check 2
                        if os.path.exists(summary_file_path):
                            print(f"article {index} scrapped, output in {output_folder}")
                        else:
                            print(f"Failed to save summary for article {index}")


