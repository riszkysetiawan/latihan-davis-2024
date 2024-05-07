import requests
import matplotlib.pyplot as plt

def get_book_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    book_titles_tags = soup.find_all('h3')
    book_titles = [tag.text for tag in book_titles_tags]
    
    book_price_tags = soup.find_all('p', class_='price_color')
    book_prices = [float(tag.text.replace('Â', '').replace('£', '')) for tag in book_price_tags]
    
    return book_titles, book_prices

url = 'https://books.toscrape.com/'

book_titles, book_prices = get_book_data(url)

plt.figure(figsize=(10, 6))
plt.barh(book_titles, book_prices, color='skyblue')
plt.xlabel('Harga (£)')
plt.ylabel('Judul Buku')
plt.title('Visualisasi Data Buku dan Harga dari https://books.toscrape.com/')
plt.gca().invert_yaxis()
plt.show()
