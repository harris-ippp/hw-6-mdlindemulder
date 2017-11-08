#!/usr/bin/env python


#addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
#resp = requests.get(addr)
#s = resp.status_code
#t = resp.text
#print(s, t)

from bs4 import BeautifulSoup as bs
import requests
ELECTION_ID = [] # Creates list
url_va = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
resp = requests.get(url_va)
html_va = resp.content
soup = bs(html_va, 'html.parser')
tags = soup.find_all('tr', 'election_item')
for t in tags:
    year = t.td.text #Gets years
    year_id = t['id'][-5:] # Gets IDs
    b = year, year_id
    ELECTION_ID.append(b)
#print(ELECTION_ID)

with open('ELECTION_ID','w') as ELECTION_ID_file:
    for line in ELECTION_ID:
        ELECTION_ID_file.write(line[0] + ' ' + line[1] + '\n') # Writes file
        #print(line[0],line[1])

#lastyear = tags[0]
#lastyear_id = lastyear['id']
#lastyear_id = lastyear['id'][-5]
