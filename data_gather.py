
#https://www.vam.ac.uk/api

#limit controls the results per page
#pad limits to objects with detailed descriptions
#images limits to objects with images
#https://www.vam.ac.uk/api/json/museumobject/search?materialsearch=silver&limit=30&pad=1&images=1

#https://www.vam.ac.uk/api
#Total number is 8902


import urllib.request, json
import csv
import pickle
import time

va_url = 'https://www.vam.ac.uk/api/json/museumobject/search?materialsearch=silver&limit=8905&pad=1&images=1'

object_nums = []

#variable for pagination
offset = 0

#this needs to be 8911, which is one more than 8910, which is a number divisible by 30 that is greater than 8902
#work through the pages to get all 8902 silver objects with images
while (offset < 8911):
    print("offset = " + str(offset))
    working_url = "https://www.vam.ac.uk/api/json/museumobject/search?materialsearch=silver&limit=8905&pad=1&images=" + str(offset)

    #creates the json
    with urllib.request.urlopen(working_url) as url:
        data = json.loads(url.read().decode())

    #adds the object number to the
    for i in data['records']:
        object_nums.append(i['fields']['object_number'])

    offset = offset + 30

    #give the server a rest
    time.sleep(.3)

#writes to CSV

with open('output.csv', mode='w') as output_file:
    file_writer = csv.writer(output_file)
    file_writer.writerow(object_nums)

#writes to pickle

with open('output', 'wb') as output_file:
    pickle.dump(object_nums, output_file)