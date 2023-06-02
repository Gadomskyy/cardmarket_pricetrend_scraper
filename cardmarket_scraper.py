import requests
from bs4 import BeautifulSoup

#Request URL
url = "https://www.cardmarket.com/en/Pokemon/Products/Singles/Lost-Origin/Pikachu-V2-LORTG05"
response = requests.get(url)

#Parse the response
soup = BeautifulSoup(response.content, "html.parser")

#Find the price trend element in soup
#Price trend is located inside labeled row class, and then in a col-6 colxl-7 class. I use soup find twice to get a list
#of all elements with that class name - there are multiple - Price trend information index is 6
price_trend_element = soup.find(class_=lambda value: value and value.startswith("labeled row")).find_all(class_=lambda value: value and value.startswith("col-6 col-xl-7"))[6].text
print(price_trend_element)
