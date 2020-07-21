#!/usr/Doreen/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 12:39:35 2019

@author: doreen
"""
import pandas as pd
import re

hotel = pd.read_csv("20190424_positive_negative_reviews.csv")


#input_string = "Mike saw a dog."
#word = "a"
def countword(input_string, word):
    count = sum(1 for _ in re.finditer(r'\b%s\b' %re.escape(word), input_string))
    return count

def PDI(nationality):
    index = country.loc[country["Country"] == nationality]["Power Distance Index"]
    if len(index) > 0:
        return float(index)
    else:
        return 'NA'

def Ind(nationality):
    index = country.loc[country["Country"] == nationality]["Individualism"]
    if len(index) > 0:
        return float(index)
    else:
        return 'NA'

#lower case 
hotel["Negative_Review"] = hotel["Negative_Review"].str.lower()
hotel["Positive_Review"] = hotel["Positive_Review"].str.lower()

#remove whitespace
hotel["Reviewer_Nationality"] = hotel["Reviewer_Nationality"].str.replace(' ', '')

#Pronouns:
hotel["count_I"] = hotel.apply(lambda row: countword(row["Negative_Review"], "i"), axis = 1)
hotel["count_me"] = hotel.apply(lambda row: countword(row["Negative_Review"], "me"), axis = 1)
hotel["count_mine"] = hotel.apply(lambda row: countword(row["Negative_Review"], "mine"), axis = 1)
hotel["count_my"] = hotel.apply(lambda row: countword(row["Negative_Review"], "my"), axis = 1)
hotel["count_we"] = hotel.apply(lambda row: countword(row["Negative_Review"], "we"), axis = 1)
hotel["count_us"] = hotel.apply(lambda row: countword(row["Negative_Review"], "us"), axis = 1)
hotel["count_our"] = hotel.apply(lambda row: countword(row["Negative_Review"], "our"), axis = 1)

#Service-relevant words for negative reviews:
hotel["count_staff"] = hotel.apply(lambda row: countword(row["Negative_Review"], "staff"), axis = 1)
hotel["count_service"] = hotel.apply(lambda row: countword(row["Negative_Review"], "service"), axis = 1)
hotel["count_check in"] = hotel.apply(lambda row: countword(row["Negative_Review"], "check in"), axis = 1)
hotel["count_check out"] = hotel.apply(lambda row: countword(row["Negative_Review"], "check out"), axis = 1)
hotel["count_receptionist"] = hotel.apply(lambda row: countword(row["Negative_Review"], "receptionist"), axis = 1)
hotel["count_impolite"] = hotel.apply(lambda row: countword(row["Negative_Review"], "impolite"), axis = 1)
hotel["count_not polite"] = hotel.apply(lambda row: countword(row["Negative_Review"], "not polite"), axis = 1)
hotel["count_rude"] = hotel.apply(lambda row: countword(row["Negative_Review"], "rude"), axis = 1)
hotel["count_waiter"] = hotel.apply(lambda row: countword(row["Negative_Review"], "waiter"), axis = 1)
hotel["count_waitress"] = hotel.apply(lambda row: countword(row["Negative_Review"], "waitress"), axis = 1)
hotel["count_personel"] = hotel.apply(lambda row: countword(row["Negative_Review"], "personel"), axis = 1)
hotel["count_reception"] = hotel.apply(lambda row: countword(row["Negative_Review"], "reception"), axis = 1)
hotel["count_gruff"] = hotel.apply(lambda row: countword(row["Negative_Review"], "gruff"), axis = 1)
hotel["count_inpatient"] = hotel.apply(lambda row: countword(row["Negative_Review"], "inpatient"), axis = 1)
hotel["count_indifferent"] = hotel.apply(lambda row: countword(row["Negative_Review"], "indifferent"), axis = 1)
hotel["count_dismissive"] = hotel.apply(lambda row: countword(row["Negative_Review"], "dismissive"), axis = 1)
hotel["count_unfriendly"] = hotel.apply(lambda row: countword(row["Negative_Review"], "unfriendly"), axis = 1)
hotel["count_unhelpful"] = hotel.apply(lambda row: countword(row["Negative_Review"], "unhelpful"), axis = 1)
hotel["count_not friendly"] = hotel.apply(lambda row: countword(row["Negative_Review"], "not friendly"), axis = 1)
hotel["count_not helpful"] = hotel.apply(lambda row: countword(row["Negative_Review"], "not helpful"), axis = 1)
hotel["count_unwelcome"] = hotel.apply(lambda row: countword(row["Negative_Review"], "unwelcome"), axis = 1)
hotel["count_not welcoming"] = hotel.apply(lambda row: countword(row["Negative_Review"], "not welcoming"), axis = 1)

#Service-relevant words for positive reviews:

hotel["count_staff_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "staff"), axis = 1)
hotel["count_service_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "service"), axis = 1)
hotel["count_check in_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "check in"), axis = 1)
hotel["count_check out_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "check out"), axis = 1)
hotel["count_receptionist_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "receptionist"), axis = 1)
hotel["count_impolite_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "impolite"), axis = 1)
hotel["count_not polite_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "not polite"), axis = 1)
hotel["count_rude_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "rude"), axis = 1)
hotel["count_waiter_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "waiter"), axis = 1)
hotel["count_waitress_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "waitress"), axis = 1)
hotel["count_personel_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "personel"), axis = 1)
hotel["count_reception_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "reception"), axis = 1)
hotel["count_gruff_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "gruff"), axis = 1)
hotel["count_inpatient_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "inpatient"), axis = 1)
hotel["count_indifferent_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "indifferent"), axis = 1)
hotel["count_dismissive_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "dismissive"), axis = 1)
hotel["count_unfriendly_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "unfriendly"), axis = 1)
hotel["count_unhelpful_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "unhelpful"), axis = 1)
hotel["count_not friendly_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "not friendly"), axis = 1)
hotel["count_not helpful_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "not helpful"), axis = 1)
hotel["count_unwelcome_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "unwelcome"), axis = 1)
hotel["count_not welcoming_1"] = hotel.apply(lambda row: countword(row["Positive_Review"], "not welcoming"), axis = 1)


#Sum all count
hotel["count_pronouns"] = hotel.iloc[:,18:25].sum(axis=1)
hotel["count_service_relevant_neg"] = hotel.iloc[:,3:24].sum(axis=1)
hotel["count_service_relevant_pos"] = hotel.iloc[:,25:47].sum(axis=1)

hotel["power_distance_index"] = hotel.apply(lambda row: PDI(row["Reviewer_Nationality"]), axis = 1)
hotel["individualism"] = hotel.apply(lambda row: Ind(row["Reviewer_Nationality"]), axis = 1)

hotel = hotel.drop(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date',
       'Average_Score', 'Hotel_Name', 'Total_Number_of_Reviews', 'Positive_Review',
       'Review_Total_Positive_Word_Counts', 'Total_Number_of_Reviews_Reviewer_Has_Given', 
       'Travel with who', 'Room type', 'Nights', 'Unnamed: 17'])

hotel.to_csv("20190424_data_new_both.csv", sep=',', index = False)

