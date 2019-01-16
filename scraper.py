import sys
import requests
import time
import os
from bs4 import BeautifulSoup


def main():
    response = requests.get("https://www.loc.gov/collections/thomas-jefferson-papers/?c=25&fa=online-format:online+text%7Csubject:correspondence&q=letter&sp=1&st=list")
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all("li", {"class": "item"})
    curr_url = response.url
    try:
        os.mkdir("Jefferson Papers")
        print("Directory 'Jefferson Papers' Created")
    except FileExistsError:
        print("Directory already made")
    page = 1
    number = 1
    while(True):
        #time.sleep(1)
        
        for item in items:
            anchor = item.find("a")
            #print(anchor["href"])
            response = requests.get(anchor["href"])
            soup1 = BeautifulSoup(response.text, 'html.parser')
            title = soup1.find("cite").decode_contents()
            view_class = soup1.find("div", {"class": "views"})
            anchor = view_class.find_all("a")[1]
            response = requests.get("https:"+anchor["href"])
            with open("Jefferson Papers/"+title+".xml", 'wb') as file:
                file.write(response.content)
            print(str(number)+ ") File '"+ title + ".xml' has been created!")
            number += 1
            response = requests.get(curr_url)
        response = requests.get(curr_url)
        page = page + 1
        #soup = BeautifulSoup(response.text, 'html.parser')
        new_page = soup.find("a", {"aria-label": "Page " + str(page)})
        if new_page == None:
            break
        response = requests.get(new_page['href'])
        curr_url = response.url
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all("li", {"class": "item"})
    print("Scraping Complete!")

if __name__ == '__main__':
    main()
