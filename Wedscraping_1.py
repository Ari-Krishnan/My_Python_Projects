from bs4 import BeautifulSoup
import openpyxl, requests
import pandas as pd

try:
    respones = requests.get('https://books.toscrape.com/')
    soup = BeautifulSoup(respones.text,'lxml')
    # print(soup.prettify())
    listings = soup.find_all(class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    # print(len(listings))
    books = []
    for listing in listings:
        book_name = listing.find('article').find('h3').a.attrs.get('title')
        book_price = listing.find('div',class_ = 'product_price').p.text
        books.append(
            {
                "Books Name" : book_name,
                "Price" : book_price
            }
        )
    df = pd.DataFrame(books)
    print(df)
    df.to_csv("Books.csv",index=False)
except Exception as e:
    print(e)
    