#!/usr/Doreen/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:02:53 2019

@author: doreen
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

data = pd.read_csv("20190323_hotel_set.csv")

hotel = []
hotel = data['Hotel_Name'] + [','] + data['Hotel_Address']

hotel_unique = hotel.unique()

def run(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    headline_results = soup.find('div', class_='oTDgte')
    if (headline_results is None) or ('hotel' not in headline_results.text):
        headline_results = 'Hotel star not found'
        return headline_results
    else:
        return headline_results.text

if __name__ == '__main__':
    results = []
    for name in hotel_unique[695:1494]:
        url = 'https://www.google.com/search?q='
        hotel_info = name
        url += hotel_info
        results.append(run(url))

hotel_star2 = pd.DataFrame(
    {'name': hotel_unique[695:1494],
     'star': results,
    })

all_data = pd.concat([hotel_star[0:695],hotel_star2])

all_data.to_csv("all_data.csv", sep=',', index = False)

############################# combine data #############################
origin = pd.read_csv("20190323_hotel_set.csv")
star = pd.read_csv("all_data.csv")

# seperate hotel name and address
star['hotel_name'] = star.apply(lambda row: row["name"].split(',')[0], axis = 1)

def add_star(hotel_name):
    index = star.loc[star["hotel_name"] == hotel_name]["star"].iloc[0]
    print(hotel_name)
    return index

origin["Hotel_Star"] = ""

for i in range(0, 467886):
    tmp = star.loc[star["hotel_name"] == origin["Hotel_Name"][i]]["star"].iloc[0]
    origin["Hotel_Star"][i] = tmp
    print(i)
    
    
origin["Hotel_Star"] = origin.apply(lambda row: add_star(row["Hotel_Name"]), axis = 1)

# origin = origin.drop(columns=["hotel_star"])

origin.to_csv("all_data_w_star.csv", sep=',', index = False)






