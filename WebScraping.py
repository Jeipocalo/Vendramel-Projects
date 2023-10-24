import requests
from bs4 import BeautifulSoup

# Page URL
url = 'https://www.bbc.com/news'

# Send HTTP to get website content
response = requests.get(url)

# Checking response Status
if response.status_code == 200:
    headlinenumber = 0
    # Analysing webpage content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Finding Headlines on the page
    news_headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')

    # Extracting and printing headlines
    for headline in news_headlines:
        headlinenumber += 1
        print(f"{headline.text}\n")
    print(f"\n\nThere are {headlinenumber} headlines.\n")
else:
    print('Failed to get response from website.')
