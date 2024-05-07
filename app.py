import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
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

# Membuat plot harga buku
fig_price, ax_price = plt.subplots(figsize=(10, 6))
ax_price.barh(book_titles, book_prices, color='skyblue')
ax_price.set_xlabel('Harga (£)')
ax_price.set_ylabel('Judul Buku')
ax_price.set_title('Visualisasi Data Buku dan Harga dari https://books.toscrape.com/')
ax_price.invert_yaxis()

# Menampilkan chart harga menggunakan Streamlit
st.pyplot(fig_price)

# Fungsi untuk mengambil data judul buku dan rating
def get_book_data_rating(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Mengambil judul buku
    book_titles_tags = soup.find_all('h3')
    book_titles = [tag.text for tag in book_titles_tags]
    
    # Mengambil rating buku
    book_rating_tags = soup.find_all('p', class_='star-rating')
    book_ratings = [tag['class'][1] for tag in book_rating_tags]
    
    return book_titles, book_ratings

# Mengambil data judul buku dan rating
book_titles_rating, book_ratings = get_book_data_rating(url)

# Membuat dataframe dari data yang diambil
df = pd.DataFrame({'Judul': book_titles_rating, 'Rating': book_ratings})

# Mengubah tipe data rating menjadi numerik
ratings_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Rating'] = df['Rating'].replace(ratings_dict).astype(float)

# Mengurutkan dataframe berdasarkan rating tertinggi
df_sorted = df.sort_values(by='Rating', ascending=False)

# Mengambil 5 buku terlaris
top_books = df_sorted.head(5)

# Membuat plot rating buku
fig_rating, ax_rating = plt.subplots(figsize=(10, 6))
ax_rating.barh(top_books['Judul'], top_books['Rating'], color='skyblue')
ax_rating.set_xlabel('Rating')
ax_rating.set_ylabel('Judul Buku')
ax_rating.set_title('5 Buku Terlaris Berdasarkan Rating Tertinggi')
ax_rating.invert_yaxis()

# Menampilkan chart rating menggunakan Streamlit
st.pyplot(fig_rating)



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

# Membuat dataframe dari data yang diambil
df = pd.DataFrame({'Judul': book_titles, 'Harga (£)': book_prices})

# Menampilkan dataframe menggunakan Streamlit
st.write(df)

# Membuat scatter plot judul buku vs harga
fig_scatter, ax_scatter = plt.subplots(figsize=(10, 6))
ax_scatter.scatter(book_titles, book_prices, color='skyblue')
ax_scatter.set_xlabel('Judul Buku')
ax_scatter.set_ylabel('Harga (£)')
ax_scatter.set_title('Scatter Plot Judul Buku vs Harga dari https://books.toscrape.com/')

# Menampilkan chart scatter plot menggunakan Streamlit
st.pyplot(fig_scatter)



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

# Membuat dataframe dari data yang diambil
df = pd.DataFrame({'Judul': book_titles, 'Harga (£)': book_prices})

# Menampilkan dataframe menggunakan Streamlit
st.write(df)

# Membuat plot menggunakan Plotly Express
fig = px.scatter(df, x='Judul', y='Harga (£)', title='Scatter Plot Judul Buku vs Harga dari https://books.toscrape.com/')
fig.update_xaxes(type='category')
fig.update_layout(xaxis_title='Judul Buku', yaxis_title='Harga (£)')
st.plotly_chart(fig)
