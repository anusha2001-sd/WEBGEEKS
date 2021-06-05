import requests
import bs4

url=input("Enter your url")
response=requests.get(url)
filename="temp.html"
bs=bs4.BeautifulSoup(response.text,"html.parser")
formatted_text=bs.prettify()
print(formatted_text)
