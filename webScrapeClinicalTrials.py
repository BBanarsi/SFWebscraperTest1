from urllib.request import urlopen as req
from bs4 import BeautifulSoup as Bsoup
import re
import requests
import urllib
import csv


url = 'https://clinicaltrials.gov/ct2/show/NCT05116943?cntry=US&state=US%3AFL&draw=2&rank=3'

# uClient = req(url)
# page_html = uClient.read()
# uClient.close()

# filename = "clinicalTrialsV1.csv"
# f = open(filename, "w")
# headers = "URL, Description, Location, Date Posted, Condition or Disease, Study Status, Contact\n"
# f.write(headers)

page_html = requests.get(url).text
soup = Bsoup(page_html, "html.parser")

#title
title_containers = soup.findAll("h1", {"class":"tr-h1"})
if len(title_containers) != 0:
    title = 'title placeholder'
else:
    title = title_containers[0].text

#description
desc_cont = soup.findAll("div", {"class":"ct-body3 tr-indent2"})
if len(desc_cont) != 0:
    desc = 'description placeholder'
else:
    desc = desc_cont[0].text

#location (Only Hosptial Working)
loc_cont = soup.findAll("td", {"headers":"locName"})
if len(loc_cont) != 0:
    loc = 'location placeholder'
else:
    loc = loc_cont[0].text

#the address isnt working yet
loc_cont2 = soup.findAll("tr", {"headers":"locName"})
# date_cont = soup.findAll("span", {"class": "term"})
# date_posted = date_cont[0].findAll("span", {"data-term": "first posted"})

#Condition not yet working
condition_title = soup.findAll("span", {"style":"display:block;margin-bottom:1ex;"})

if len(condition_title) != 0:
    condition = 'Condition placeholder'
else:
    condition_name = str(condition_title[0].text)
    condition = condition_name
print(condition)
#Date Poste
date_first_posted = soup.findAll("div", {"style":"font-size:inherit"})
if len(date_first_posted) != 0:
    date_1st_posted = 'Date placeholder'
else:
    date_1st_posted = str(date_first_posted[0].text)
date = date_1st_posted.removeprefix('\nFirst Posted  : ')

#Study Status
status_cont = soup.findAll("td", {"headers":"locStatus"})
if len(status_cont) != 0:
    status = 'Status placeholder'
else:
    status = status_cont[0].text

#contact info
contact_info_cont = soup.findAll("td", {"style":"padding:0;padding-left:4em"})
if len(contact_info_cont) != 0:
    contact = 'Contact placeholder'
else:
    contact_info = str(contact_info_cont[0].text.strip())
    contact = contact_info.removeprefix('Contact: ')

#Print
#f.write(url + "," + desc + "," + loc + "," + date + "," + condition + "," + status + "," + contact + "\n")
#print(contact)




# tr = table.tbody.find_all("tr")
#tr = soup.find("tr", attrs={"class":"odd parent"})
#tr = soup.find(id='theDataTable').find('tbody').find_all('tr')
#tr_data = soup.findAll("tr", {"class":"odd parent"})
#table_data = table.find_all('tbody')
#t_body = table.thead

# for rows in tr:
# 	data = rows.find_all('td')
# 	print(data)



# for table in tables:
# 	tr_tags = table.find_all('tr')

# 	for tr in tr_tags:
# 		td_tags = tr.find_all('td')

# 		for td in td_tags:
# 			text = td.string
			

# print(tr_tags)



