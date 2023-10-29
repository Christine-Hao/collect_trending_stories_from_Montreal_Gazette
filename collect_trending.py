from pathlib import Path
import requests
import bs4


def get_news_html_page_data(newspaper_name, newspaper_main_page):
    fpath = Path(f"{newspaper_name}.html")

    if not fpath.exits():
        data = requests.get(f"{newspaper_main_page}")


def main():
    get_news_html_page_data("Montreal_Gazette", "https://montrealgazette.com/")
