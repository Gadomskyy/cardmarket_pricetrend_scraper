import requests
from bs4 import BeautifulSoup
import csv

def create_pricelist(csv_file, column_index, condition_value):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row

        #create list to hold all price values
        pricelist = []

        for row in reader:
            value = row[column_index]
            response = requests.get(row[2])
            # Parse the response
            soup = BeautifulSoup(response.content, "html.parser")
            if value == condition_value:
                # Find the price trend element in soup
                # Price trend is located inside labeled row class, and then in a col-6 colxl-7 class. I use soup find twice to get a list
                # of all elements with that class name - there are multiple - Price trend information index is 6 for Pokemon, 5 for trainers (different layout)
                price_trend_element = soup.find(class_=lambda value: value and value.startswith("labeled row")).find_all(class_=lambda value: value and value.startswith("col-6 col-xl-7"))[6].text
                pricelist.append(price_trend_element)
            else:
                price_trend_element = soup.find(class_=lambda value: value and value.startswith("labeled row")).find_all(class_=lambda value: value and value.startswith("col-6 col-xl-7"))[5].text
                pricelist.append(price_trend_element)
    return pricelist



print(check_column_value('cardlist.csv', 3, 'Y'))

