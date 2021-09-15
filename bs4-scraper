import requests
from bs4 import BeautifulSoup
import os
import os.path



def get_input_url():
    pages_requested = int(input())
    article_requested = input()
    saved_articles = []
    for i in range(1, pages_requested + 1):
        path = 'Page_' + str(i)
        starting_work_dir = os.getcwd()
        os.mkdir(path)
        os.chdir(starting_work_dir + f'/{path}')
        url = 'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page=' + str(i)
        status_code = requests.get(url).status_code
        if status_code < 399:
            page_content = requests.get(url).content
            soup = BeautifulSoup(page_content, 'html.parser')
            for x in soup.find_all('article'):
                article_type = x.div.find_next_sibling('div').span.span.text
                if article_type == article_requested:
                    article_name = str(x.div.h3.a.text).replace(' ', '_').rstrip().replace('?', '')
                    article_hyperlink = x.div.h3.a['href']
                    with open(f'{article_name}.txt', 'w', encoding='UTF-8') as file:
                        saved_articles.append(article_name)
                        article_url = 'https://www.nature.com' + article_hyperlink
                        page_content = requests.get(article_url).content
                        soup = BeautifulSoup(page_content, 'html.parser')
                        if article_type == 'News':
                            find_body = soup.find('div', {'class': 'c-article-body'}).text.strip().replace('\n', '')
                        else:
                            find_body = soup.find('div', {'class': 'article-item__body'}).text.strip().replace('\n', '')
                        file.write(find_body)
                        print('Article Saved')
                        file.close()
        os.chdir(starting_work_dir)

    else:
        pass


get_input_url()
