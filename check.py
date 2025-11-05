import requests

author = "J.K. Rowling"
url = f'https://www.googleapis.com/books/v1/volumes?q=inauthor:{author}'
response = requests.get(url)
data = response.json()
print(data)
