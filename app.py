import streamlit as st
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Fungsi untuk mengambil data judul buku dan harga
def get_book_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Mengambil judul buku
    book_titles_tags = soup.find_all('h3')
    book_titles = [tag.text for tag in book_titles_tags]
    
    # Mengambil harga buku
    book_price_tags = soup.find_all('p', class_='price_color')
    book_prices = [float(tag.text.replace('Â', '').replace('£', '')) for tag in book_price_tags]
    
    return book_titles, book_prices

# URL dari website yang akan di-scrape
url = 'https://books.toscrape.com/'

# Mengambil data judul buku dan harga
book_titles, book_prices = get_book_data(url)

# Membuat plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(book_titles, book_prices, color='skyblue')
ax.set_xlabel('Harga (£)')
ax.set_ylabel('Judul Buku')
ax.set_title('Visualisasi Data Buku dan Harga dari https://books.toscrape.com/')
ax.invert_yaxis()

# Menampilkan chart menggunakan Streamlit
st.pyplot(fig)


import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Fungsi untuk mengambil data judul buku dan rating
def get_book_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Mengambil judul buku
    book_titles_tags = soup.find_all('h3')
    book_titles = [tag.text for tag in book_titles_tags]
    
    # Mengambil rating buku
    book_rating_tags = soup.find_all('p', class_='star-rating')
    book_ratings = [tag['class'][1] for tag in book_rating_tags]
    
    return book_titles, book_ratings

# URL dari website yang akan di-scrape
url = 'https://books.toscrape.com/'

# Mengambil data judul buku dan rating
book_titles, book_ratings = get_book_data(url)

# Membuat dataframe dari data yang diambil
df = pd.DataFrame({'Judul': book_titles, 'Rating': book_ratings})

# Mengubah tipe data rating menjadi numerik
ratings_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Rating'] = df['Rating'].replace(ratings_dict).astype(float)

# Mengurutkan dataframe berdasarkan rating tertinggi
df_sorted = df.sort_values(by='Rating', ascending=False)

# Mengambil 5 buku terlaris
top_books = df_sorted.head(5)

# Menampilkan data 5 buku terlaris dalam bentuk bar chart
plt.figure(figsize=(10, 6))
plt.barh(top_books['Judul'], top_books['Rating'], color='skyblue')
plt.xlabel('Rating')
plt.ylabel('Judul Buku')
plt.title('5 Buku Terlaris Berdasarkan Rating Tertinggi')
plt.gca().invert_yaxis()
plt.show()
