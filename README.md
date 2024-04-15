# KSDK News Article Scrapper - Godfred Adjei-Darko

The **KSDK News Article Scraper** is a Python file that reads a file containing article links, retrieves the content of each article, and saves the information (headline, author, summary, and article text) to individual text files in numerical order (from 1).

## Prerequisites

1. Python 
Ensure you have python installed. You can find the python download at [www.python.org/downloads/](https://www.python.org/downloads//)

2. Conda 
In order to set up the scrapper environment needed for the article scrapper, anaconda/miniconda is required. 
You can find miniconda at https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html, along with instructions on 
how to set up miniconda on windows, macOS, and linux

## Conda to VS Code for Windows
If you are looking to connect the conda to vscode on windows, first open the "anaconda prompt" and type the command "where conda" inside the anaconda prompt to find the paths related to your conda installastion. 
Next, in the windows search bar, search for advanced system settings and select "view advanced system settings" to which you will select environment variables. 
Afterward, click on "Path" then "Edit..." then "New", which will take you to the edit environment variable.
From here, include the paths related to your conda installation.
Paths to include:
    C:\Users\userName\Anaconda3\Scripts
    C:\Users\userName\Anaconda3
    C:\Users\userName\Anaconda3\Library\bin
    C:\Users\userName\Anaconda3\Library\mingw-w64\bin (if it is there in your system)
    C:\Users\userName\Anaconda3\Library\user\bin (if it is there)
where "userName" and "Aanaconda3" are placeholders for your system username and the file of your conda installation respectively (will be miniconda3 if miniconda is installed)
To Confirm Setup, open up the Anaconda promp and type "conda --version"

3. Set up the Conda Environment
In order to set up the scrapper environment given you have installed conda, you must create the environment from the
provided requirements.yaml file. 

In the conda command console, type conda env create -f requirements.yaml. The "scrapper" environment will be created. 
Double check with conda env list to ensure that the scrapper environment has been created.

## Program Steps

1. Create .txt file with links
First, create a .txt with all the ksdk news article links (new line terminated). See the "articles.txt" for an example.
   * Note, you can also use the articles.txt file and just replace the links with your links

2. In the vscode terminal, type "python run.py". You will be prompted to input the .txt file name. Input the full file name (example: articles.txt) If the file is invalid, "File XYZ is not found" will be printed meaning your cannot be found. 

3. Next, all the articles links will be processed and output to individual .txt files starting from article_1.txt in the Data/processed folder. If a link is invalid, the link will be skipped with an output message and the other files will be created.

## OpenAI Article Summary
In order to properly create an OpenAI summay of an article, you must first 

1. Add your api key (from https://platform.openai.com/api-keys). You must create an account (or log in), and create an Api Key.

2. Put your Api Key into "ai_summary.py" located in "module_3". On line four, which has "client = OpenAI(api_key="ADD API KEY HERE")", replace "ADD API KEY HERE" with your Api Key in quotation marks (" ").

After completeing these steps, the ai summary will be generated when running the program with the text prompt "Summary for "artile #" saved to some file path"
