from urllib.request import urlopen as req
from bs4 import BeautifulSoup as Bsoup
import requests
import pandas as pd

df = pd.read_csv("SearchResults.csv")
idnum = df.NCTNumber.tolist()
i=0

filename = "clinicalTrialsV1.csv" 
f = open(filename, "w")
headers = "URL, Description, Location, Date Posted, Condition or Disease, Study Status, Contact\n"
f.write(headers)

for row in df:
    url = 'https://clinicaltrials.gov/ct2/show/'+idnum[i]+'?cntry=US&state=US%3AFL&draw=2&rank='+str(i+1)+''
    print(url)
   
    page_html = requests.get(url).text
    soup = Bsoup(page_html, "html.parser")

    #title
    title_containers = soup.findAll("h1", {"class":"tr-h1"})
    if len(title_containers) == 0:
        title = 'title placeholder'
    else:
        title = str(title_containers[0].text)
        title =title.replace(',', '')

    #description
    desc_cont = soup.findAll("div", {"class":"ct-body3 tr-indent2"})
    if len(desc_cont) == 0:
        desc = 'description placeholder'
    else:
        desc = str(desc_cont[0].text)
        desc = desc.replace(',', '')

    #location (Only Hosptial Working)
    loc_cont = soup.findAll("td", {"headers":"locName"})
    if len(loc_cont) == 0:
        loc = 'location placeholder'
    else:
        loc = str(loc_cont[0].text)
        loc = loc.replace(',', '')

    #the address isnt working yet
    loc_cont2 = soup.findAll("tr", {"headers":"locName"})
    # date_cont = soup.findAll("span", {"class": "term"})
    # date_posted = date_cont[0].findAll("span", {"data-term": "first posted"})

    #Condition not yet working
    condition_title = soup.findAll("span", {"style":"display:block;margin-bottom:1ex;"})
    if len(condition_title) == 0:
        condition = 'Condition placeholder'
    else:
        condition_name = str(condition_title[0].text)
        condition = condition_name
        
    #Date Posted
    date_first_posted = soup.findAll("div", {"style":"font-size:inherit"})
    if len(date_first_posted) == 0:
        date = 'Date placeholder'
    else:
        date_1st_posted = str(date_first_posted[0].text)
        date = date_1st_posted.removeprefix('\nFirst Posted  : ')
        date = date.replace(',', '')

    #Study Status
    status_cont = soup.findAll("td", {"headers":"locStatus"})
    if len(status_cont) == 0:
        status = 'Status placeholder'
    else:
        status = str(status_cont[0].text)
        status = status.replace(',', '')

    #contact info
    contact_info_cont = soup.findAll("td", {"style":"padding:0;padding-left:4em"})
    if len(contact_info_cont) == 0:
        contact = 'Contact placeholder'
    else:
        contact_info = str(contact_info_cont[0].text.strip())
        contact = contact_info.removeprefix('Contact: ')

        contact = contact.replace(',', '')
    #Print
    f.write(url + "," + desc + "," + loc + "," + date + "," + condition + "," + status + "," + contact + "\n")
    i=i+1

# print(df)
# with open('SearchResults.csv', newline='') as csvfile:
#      filereader = csv.reader(csvfile)
#      for row in filereader:
#          print(','.join(row))