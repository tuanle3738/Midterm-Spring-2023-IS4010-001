# main.py

# Name: Tuan Le
# email: le2te@mail.uc.edu    
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This module sends an API request then prints out some information
# Citations: Code and guide from Professor Nicholson
# Anything else that's relevant: My API key is gEOeqq1LwIMU9Gpqe1Fd1G7bdS9JvgPLYLDcMbL5

import json
import requests

# Send the data request
response = requests.get('https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=id,school.name,2013.student.size&api_key=gEOeqq1LwIMU9Gpqe1Fd1G7bdS9JvgPLYLDcMbL5')

# Parse the results into a Python dictionary
json_string = response.content
parsed_json = json.loads(json_string) # Now we have a python dictionary

#print(parsed_json)
#print(parsed_json['data'][0]['description'])
#print(parsed_json['data'][0]['directionsInfo'])
#total = int(parsed_json['total']) # The number of parks that were returned

# print out how many students each school has in 2013
for school in parsed_json['results']:
    print (school['school.name'], 'has', school['2013.student.size'], 'students in 2013')
