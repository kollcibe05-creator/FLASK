import requests # pipenv install
import json # standard library

response = requests.get("https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json")
print(response.text)
print(json.loads(response.content))

json_content = json.loads(response.content)
print(json.dumps(json_content, indent=4, sort_keys=True))

class Search:

    def get_search_results(self):
        seach_term = "the lord of the rings"

        search_term_formatted = seach_term.replace(" ", "+")

        fields = ["title", "author_name"]

        fields_formatted = ','.join(fields) # join them to get 'title,author_name'

        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        response = requests.get(URL)

        return response.content

response = Search().get_search_results()
print(results)


    def get_search_results_json(self):

        seach_term = "the lord of the rings"

        search_term_formatted = seach_term.replace(" ", "+")

        fields = ["title", "author_name"]

        fields_formatted = ','.join(fields) # join them to get 'title,author_name'

        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        print(URL)

        response = requests.get(URL)

        return response.json()


results_json = Search().get_search_results_json()

print(json.dumps(results_json, indent=1))

    def formatted_output(self):
        response = self.get_search_results_json()
        response_formatted = f"Title: {response['docs'][0]['title']}\nAuthor: {response['docs'][0]['author_name'][0]}"
        return response_formatted
    
search_term = input("Enter a book title: ")
result = Search().get_search_results(search_term)
print("Search Result:\n")
print(result)
