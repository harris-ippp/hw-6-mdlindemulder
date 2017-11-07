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





#for id in open("ELECTION_ID.txt", "r"):
#    base = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
#    year = id[:4]
#    year_id = id[5:]
##    lastyear_text = requests.get(lastyear_url).text
#    file_name = year +".csv"
#    with open(file_name, "w") as out:
#        out.write(lastyear_text)





#with open('president_general_2016.csv', 'w') as output:
#    output.write(requests.get(lastyear_url).text)

    #lastyear = tags[0]
    #lastyear_id = lastyear['id']
    #lastyear_id = lastyear['id'][-5]
