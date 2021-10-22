from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#open connection and download webpage
myurl = 'https://www.newegg.com/p/pl?d=graphics+card'

uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

#Parses the raw html data file taken from myurl

page_soup = soup(page_html, "html.parser")

# loop through everything on the page and grab back the title
containers = page_soup.findAll("div", {"class":"item-cell"})

for container in containers:
	brand = container.div.div.div.a.img["title"]
	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text
	print("brand: " + brand)
	print("product_name: " + product_name)
