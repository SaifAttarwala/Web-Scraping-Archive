# bs4 is BeautifulSoup Version 4, im using this library to parse through webpages with relative ease
# pip install beautifulsoup4
# I also used the requests module which could be installed with "pip install requests"
# This is just like the javascript req.get function on nodejs

from bs4 import BeautifulSoup
import requests
#########################################################################
# with open('C:/Users/DARKSOUL/Desktop/home.html', 'r') as html_file:

#     content = html_file.read()
#     soup = BeautifulSoup(content, 'lxml')

#     courses = soup.find_all('div', class_='card')

#     for x in courses:
#         name = x.h5.text
#         price = x.a.text.split()[-1]

#         # print(name)
#         # print(price)

#         print(f'{name} costs {price}')
##########################################################################


# The code below parses the website with classes and defined keywords to filter out
# jobs which are posted "Few days ago" and lists them nicely altogether

html_page = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

# print(html_page)

soup = BeautifulSoup(html_page, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    company = job.find('h3', class_='joblist-comp-name').text.strip()
    skills = job.find(
        'span', class_='srp-skills').text.strip().replace(" ", "").replace(",", ", ")
    date = job.find('span', class_='sim-posted').text.strip()

    if date == "Posted few days ago":
        print(f'''
          Name: {company}
          Skills required: {skills}
          Posted: {date}
          ''')
