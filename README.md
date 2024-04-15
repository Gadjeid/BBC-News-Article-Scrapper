# KSDK News Article Scraper - Godfred Adjei-Darko

The **KSDK News Article Scraper** is a Python program that reads a file containing article links, retrieves the content of each article, and saves the information (headline, author, summary, and article text) to individual text files in numerical order (starting from 1).

## Prerequisites

1. **Python**: Ensure you have Python installed. You can download Python from [www.python.org/downloads/](https://www.python.org/downloads/).

2. **Conda**: To set up the scraper environment needed for the article scraper, Anaconda/Miniconda is required. You can download Miniconda from [here](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html), along with instructions on how to set it up on Windows, macOS, and Linux.

## Connecting Conda to VS Code for Windows

If you are looking to connect Conda to VS Code on Windows, follow these steps:

1. Open the "Anaconda Prompt" and type the command `where conda` to find the paths related to your Conda installation.
2. In the Windows search bar, search for advanced system settings and select "View Advanced System Settings". Then, select "Environment Variables".
3. Click on "Path", then "Edit...", then "New", which will take you to the Edit Environment Variable window.
4. Include the paths related to your Conda installation. Paths to include are:
    - C:\Users\userName\Anaconda3\Scripts
    - C:\Users\userName\Anaconda3
    - C:\Users\userName\Anaconda3\Library\bin
    - C:\Users\userName\Anaconda3\Library\mingw-w64\bin (if it exists in your system)
    - C:\Users\userName\Anaconda3\Library\user\bin (if it exists)
   
   Replace "userName" and "Anaconda3" with your system username and the folder of your Conda installation respectively (will be Miniconda3 if Miniconda is installed).
5. To confirm the setup, open up the Anaconda prompt and type `conda --version`.

## Setting Up the Conda Environment

To set up the scraper environment, given you have installed Conda, you must create the environment from the provided `requirements.yaml` file. 

In the Conda command console, type `conda env create -f requirements.yaml`. The "scraper" environment will be created. Double-check with `conda env list` to ensure that the scraper environment has been created.

## Program Steps

1. **Create .txt file with links**: First, create a .txt file with all the KSDK news article links (new line terminated). See the "articles.txt" for an example. Note, you can also use the articles.txt file and just replace the links with your links.
2. **Run the program**: In the VS Code terminal, type `python run.py`. You will be prompted to input the .txt file name. Input the full file name (example: articles.txt). If the file is invalid, "File XYZ is not found" will be printed, meaning your file cannot be found. 
3. **Process the articles**: Next, all the article links will be processed and output to individual .txt files starting from article_1.txt in the Data/processed folder. If a link is invalid, the link will be skipped with an output message and the other files will be created.

## OpenAI Article Summary

To properly create an OpenAI summary of an article, you must first:

1. Add your API key (from [OpenAI API Keys](https://platform.openai.com/api-keys)). You must create an account (or log in), and create an API Key.
2. Put your API Key into "ai_summary.py" located in "module_3". On line four, which has `client = OpenAI(api_key="ADD API KEY HERE")`, replace "ADD API KEY HERE" with your API Key in quotation marks (" ").

After completing these steps, the AI summary will be generated when running the program with the text prompt "Summary for article # saved to some file path".
