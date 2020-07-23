"""
This is a example that scrapes the IOE Website only fetching the notices
This idea can be used to provide the content from IOE website into the mobile app , web app , dekstop app etc... by creating the rest api
"""
# Importing required modules
import requests as rq
from bs4 import BeautifulSoup as bs

# Variables

#Select Desired page number upto which you want to scrape inside the while loop condition
pageNumber = 1
#Header counter to use as heading number
headerCounter = 1

# Main Method

pagesToScrape = input('Enter Number of Pages to Scrap:')
print('\n')

while(pageNumber<int(pagesToScrape)):
    url = 'https://exam.ioe.edu.np/?page='+str(pageNumber)
    # request object that contains the whole website markups
    req = rq.get(url)
    #calling BeautifulSoup
    soup = bs(req.text, 'lxml')
    # Initializing the empty list for headers=Title and Link respectively
    headersList = []
    linksList = []
    #The scraped link misses this strings 
    urlToMergeWithLink = 'https://exam.ioe.edu.np/'

    # Scraping here

    for i in soup.findAll('span', {'class': ''}):
        headersList.append(i.text)
        # span lies as the child of the a href so previous of span is a href
        # comb contains both the headers and href links attached
        comb = i.find_previous('a')
        # only extracting the href content from the comb object
        receivedHrefLink = comb['href']
        linksList.append(urlToMergeWithLink + receivedHrefLink)

    # Displaying the captured headers and links

    for i in range(0, len(headersList)):
        print(str(headerCounter)+':'+headersList[i]+'\n'+linksList[i])
        print('\n')
        headerCounter = headerCounter + 1
    
    pageNumber = pageNumber + 1


a = input('Press Any Key to Exit')

