#!/usr/bin/env python
import glob
import pandas as pd
%matplotlib inline


# I tried this and I am still not sure why it didnt' work
for x in range(1924, 2020, 4):
    header = pd.read_csv('president_general_{}.csv', nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv('president_general_{}.csv', index_col = 0, thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df['Year'] = {}
    df['Republican Share'] = df['Republican']/df['Total Votes Cast']

df["Accomack County"].plot(kind = line)
plt.title("Share of Republican Vote 1924-2016 Accomack County") # Creates title
plt.xlabel("Year") # Creates x-axis label
plt.ylabel("Republican Share") # Creates y-axis label
plt.savefig('accomack_county.pdf')

df["Albermarle County"].plot(kind = line)
plt.title("Share of Republican Vote 1924-2016 Albermarle County") # Creates title
plt.xlabel("Year") # Creates x-axis label
plt.ylabel("Republican Share") # Creates y-axis label
plt.savefig('albermarle_county.pdf')

df["Alexandria City"].plot(kind = line)
plt.title("Share of Republican Vote 1924-2016 Alexandria City") # Creates title
plt.xlabel("Year") # Creates x-axis label
plt.ylabel("Republican Share") # Creates y-axis label
plt.savefig('alexandria_city.pdf')

df["Alleghany County"].plot(kind = line)
plt.title("Share of Republican Vote 1924-2016 Alleghany County") # Creates title
plt.xlabel("Year") # Creates x-axis label
plt.ylabel("Republican Share") # Creates y-axis label
plt.savefig('alleghany_county.pdf')


# I tried the code below, but could not figure out how to make the necessary changes
path = '/Users/mdlindemulder/Documents/UChicago/Courses/Programming/Assignments/hw-6-mdlindemulder-master'
    allFiles = glob.glob(path + '/*.csv')
    frame = pd.DataFrame()
    election = []
    for race in allFiles:
        df = pd.read_csv(race, index_col = 0, header = 0)
        election.append(df)
    frame = pd.concat(election)
    df['Republican Share'] = df['Republican']/df['Total Votes Cast']
