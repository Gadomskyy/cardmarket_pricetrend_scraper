import requests
from bs4 import BeautifulSoup
import csv

#Read links to cards from csv file
def read_csv_column(csv_file, column_name):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        column_data = []
        for row in reader:
            column_data.append(row[column_name])
    return column_data

link_list = read_csv_column('cardlist.csv', 'Link')


def check_column_value(csv_file, column_index, condition_value):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row

        for row in reader:
            value = row[column_index]
            response = requests.get(row[2])
            # Parse the response
            soup = BeautifulSoup(response.content, "html.parser")
            if value == condition_value:
                # Find the price trend element in soup
                # Price trend is located inside labeled row class, and then in a col-6 colxl-7 class. I use soup find twice to get a list
                # of all elements with that class name - there are multiple - Price trend information index is 6 for Pokemon, 5 for trainers
                price_trend_element = soup.find(class_=lambda value: value and value.startswith("labeled row")).find_all(class_=lambda value: value and value.startswith("col-6 col-xl-7"))[6].text
                print(price_trend_element)
            else:
                price_trend_element = soup.find(class_=lambda value: value and value.startswith("labeled row")).find_all(class_=lambda value: value and value.startswith("col-6 col-xl-7"))[5].text
                print(price_trend_element)



with open('cardlist_result.csv', 'w') as file:
        check_column_value('cardlist.csv', 3, 'Y')
