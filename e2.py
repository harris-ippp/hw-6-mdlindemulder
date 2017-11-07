#!/usr/bin/env python

for line in open("ELECTION_ID", "r"):
    base = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
    year = line[:4]
    year_id = line[-6:-1]
    lastyear_url = base.format(year_id)
    lastyear_text = requests.get(lastyear_url).text
    file_name = "president_general_" + year +".csv"
    with open(file_name, "w") as out:
        out.write(lastyear_text)


#from bs4 import BeautifulSoup as bs
#import requests
#ELECTION_ID = []
#url_va = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
#resp = requests.get(url_va)
#html_va = resp.content
#soup = bs(html_va, 'html.parser')

#tags = soup.find_all('tr', 'election_item')

#for t in tags:
#    year = t.td.text
#    year_id = t['id'][-5:]
#    b = [year, year_id]
#    ELECTION_ID.append(b)
#    print(year, year_id)


#for id in open("ELECTION_ID.txt", "r"):
#    base = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
#    year = id[:4]
#    year_id = id[5:]
##    lastyear_text = requests.get(lastyear_url).text
#    file_name = year +".csv"
#    with open(file_name, "w") as out:
#        out.write(lastyear_text)

#d = dict(zip(year_id, year))

#for id in year_id:
#    base = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
#    lastyear_url = base.format(id)
#    lastyear_text = requests.get(lastyear_url).text
#    file_name = d[id] + ".csv"

#    with open(file_name, 'w') as output:
#        output.write(lastyear_text)

#with open('president_general_2016.csv', 'w') as output:
#    output.write(requests.get(lastyear_url).text)

    #lastyear = tags[0]
    #lastyear_id = lastyear['id']
    #lastyear_id = lastyear['id'][-5]
