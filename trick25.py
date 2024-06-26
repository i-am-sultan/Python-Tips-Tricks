import requests
from bs4 import BeautifulSoup

def fetch_news_from_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')  # This depends on the website structure
        return articles
    else:
        print(f"Failed to fetch news: {response.status_code}")
        return []

def display_news(articles):
    for article in articles:
        title = article.find('h2').text if article.find('h2') else 'No title'
        description = article.find('p').text if article.find('p') else 'No description'
        print(f"Title: {title}")
        print(f"Description: {description}")
        print("-" * 80)

if __name__ == "__main__":
    url = 'https://minervadb.xyz/how-to-avoid-a-mutating-table-happening-in-postgresql/#:~:text=Avoid%20triggers%20that%20modify%20the,that%20they%20are%20executed%20atomically.'
    articles = fetch_news_from_website(url)
    display_news(articles)
