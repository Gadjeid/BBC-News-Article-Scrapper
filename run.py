# Run.py file that imports the other modules and runs the file
# Calls module 1 to read file and module 2 to process links from file
# Single Responsibility Principle, run.py only servers to call the modules and link the whole program together.
# The module does not change or alter the overall program or the individual modules

from module_1 import file_open as file_read
from module_2 import link_process as process
from module_3 import ai_summary as summary
def main():
    article_links = file_read.read_file()
    # Test case 2: Check if article_links are read
    if article_links:
        process.soup_scrap(article_links)
        next_step = input("Summarize with OpenAI? (Y / N): ")
        if next_step.lower() == 'y':
            summary.summarize_articles()
    else:
        print("No article links found.")

    

if __name__ == "__main__":
    main()
