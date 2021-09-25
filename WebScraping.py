import requests 
from bs4 import BeautifulSoup as bs

#user = input("enter the user name : ")
user = "Moha-boukhatem"
link = "https://github.com/"+user
result = requests.get(link)

src = result.content

sourceCode  = bs(src,'lxml')
#print(code.prettify())

pics = sourceCode.find_all("img")
for pic in pics:
    print(pic.get('src'))
    
