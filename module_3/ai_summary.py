# Import openai (to make use of the LLM) and supply an API key
import os
from openai import OpenAI
client = OpenAI(api_key="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")

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
    output_folder = 'Data/processed/summaries'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    articles_path = 'Data/processed'
    for index, file_name in enumerate(os.listdir(articles_path), start=1):
        if file_name.endswith('.txt'):
            with open(os.path.join(articles_path, file_name), 'r') as file:
                lines = file.readlines()
                title = None
                content = ""
                for line in lines:
                    if line.startswith("Headline: "):
                        title = line[len("Headline: "):].strip()
                    else:
                        content += line
                if title is not None:
                    summary = summarize(content)

                    summary_file_path = os.path.join(output_folder, f'article_{index}_summary.txt')
                    with open(summary_file_path, 'w') as summary_file:
                        summary_file.write(f"Headline: {title}\n")
                        summary_file.write(summary)
                        print(f'Summary for "artile {index}" saved to {summary_file_path}.')


