from turtle import ht
from bs4 import BeautifulSoup
import requests
# bs4(BeautifulSoup4) can also be downloaded as pipenv install beautifulsoup4 then imported as above. It boils down to preference and convention incase of misconfigs. 
headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

# html_ = requests.get("https://google.com")
# print(html_.text)

# Types of Python objects pertinent to BeautifulSoup
# Tag, NavigableString, BeautifulSoup, Comment, ResultSet

# 403, means Forbidden. The site may be trying to prevent bots. That is why you have to include the headers with `user-agent`
html_ = requests.get('https://flatironschool.com/', headers=headers)
print(html_)

doc = BeautifulSoup(html_.text, 'html.parser')
print(doc)

print(doc.select(".header")[0].contents)
print(doc.select('.header')[0].contents.strip())
print(doc.select('.header')[0].text)


# working with bs4.element.Tag
print(doc.select(".display-2.mt-6.text-brand-blue")[0].name) # literal name tag # => h2
print(doc.select(".display-2.mt-6.text-brand-blue")[0].attrs) # returns ids, names, classes and other useful content like alt and src for images
print(doc.select(".display-2.mt-6.text-brand-blue")[0].children) # returns ids, names, classes and other useful content like alt and src for images

print(doc.select(".display-2.mt-6.text-brand-blue")[0].select('span')[0].text)

print(doc.select(".display-2.mt-6.text-brand-blue")[0].select('span')[0].contents[0].strip())
# note that there is no space in the class name. `.` are used instead