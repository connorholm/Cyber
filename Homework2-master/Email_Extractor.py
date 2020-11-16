#Email_Extractor.py
#Name:
#Date:
#Assignment:

import requests
from bs4 import BeautifulSoup

def filterNoneType(lis):
    lis2 = []
    for l in lis: #filter out NoneType
        if type(l) == str:
            lis2.append(l)
    return lis2

def checkIfDuplicates(listOfElems, ele):
    ''' Check if given list contains any duplicates '''
    for elements in listOfElems:
      if elements == ele:
        return False
    return True

def main():
  #prompt the user for a webpage url
  url = input("Enter a URL to get emails off of: ")
  #url = 'https://www.unomaha.edu/college-of-information-science-and-technology/about/faculty-staff/index.php'
  url_html = requests.get(url)

  soup = BeautifulSoup(url_html.text, "html.parser")
  info = soup.find_all(class_="col-sm-10")
  
  #Convert the soup to a string version
  liInfos = []
  links = []
  newLinks = []
  for li in info:
    liInfo = li.find_all("li")
    liInfos.append(liInfo)
  for link in soup.find_all("a"):
    links.append(link.get("href"))
  links = filterNoneType(links)
  #Not_none_values = filter(None.__ne__, links)
  #links = list(Not_none_values)
  for link in links:
    if link[0:4] == "http" or link[0:3] == "../" or link[0:1] == "#" or link[0:4] == "tel:":
      continue
    for letter in link:
      if letter == "@" and link[1] != "@" and link[-1] !=  "@":
        if link[0:4] == "mail":
          newLinks.append(link[8:])
          continue
        if checkIfDuplicates(links, link) == False:
          newLinks.append(link)
  if newLinks == []:
    print("No emails found :(")
  else:
    print(newLinks)
   
  #Split the text into a list, with the end of line \n as the delimiter
  #print(liInfos)
  #print(links)

main()
