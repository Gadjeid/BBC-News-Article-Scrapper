from module_1 import file_open as file_read
from module_2 import link_process as process
def main():
    article_links = file_read.read_file()
    if article_links:
        process.soup_scrap(article_links)
    else:
        print("No article links found.")

if __name__ == "__main__":
    main()