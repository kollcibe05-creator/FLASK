from bs4 import BeautifulSoup
import requests
from Course import Course
import ipdb


class Scraper:
    def __init__(self):
        self.courses = []
    def get_page(self):
        doc = BeautifulSoup(
            requests.get('http://learn-co-curriculum.github.io/site-for-scraping/courses').text, 
            'html.parser'
        )
        # ipdb.set_trace() # try prompting doc.content, doc.text...
        # return doc
        # print(doc.select('.post')) # the <articles> of each course # returns a list of their tags with all the info.
        # print(doc.select('.post')[0]) # to inspect course details
        # Even better 'Inspect' on the browser
        # print(doc.select('.post')[0].select('h2')) # => [<h2>Web Development Immersive</h2>]
        # print(doc.select('.post')[0].select('h2')[0].text)
        # print(doc.select('.post')[0].select('.date')[0].text)
        # print(doc.select('.post')[0].select('p')[0].text)
        course_list = [] # personal test case
        for course in doc.select('.post'):
            print(type(course)) # <class 'bs4.element.Tag'>

            title = course.select("h2")[0].text if course.select("h2") else ''
            date = course.select('.date')[0].text if course.select('.date') else ''
            description = course.select('p')[0].text if course.select('p') else ''

            dict_ = {}
            dict_['title'] = title
            dict_['date'] = date                # personal test case
            dict_['description'] = description
            course_list.append(dict_)


            new_course = Course(title, date, description)
            self.courses.append(new_course)
        print(course_list)

        


scraper = Scraper()
# print(scraper.courses)
print(Course)

# Refactored Scraper

class Scraper:
    def __init__(self):
        self.courses = []
    def get_page(self):
        doc = BeautifulSoup(
            requests.get('http://learn-co-curriculum.github.io/site-for-scraping/courses').text, 
            'html.parser'
        )
        #ipdb.set_trace()
        return doc

    def get_courses(self):
        return self.get_page().select('.post')
    def make_courses(self):
        for course in self.get_courses():
            title = course.select("h2")[0].text if course.select("h2") else ''
            date = course.select('.date')[0].text if course.select('.date') else ''
            description = course.select('p')[0].text if course.select('p') else ''

            new_course = Course(title, date, description)
            self.courses.append(new_course)
        return self.courses
    def print_courses(self):
        for course in self.make_courses():
            print(course)

scraper = Scraper()

print(scraper.print_courses())