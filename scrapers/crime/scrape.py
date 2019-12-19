import csv
import requests
from bs4 import BeautifulSoup

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content
# print(html)

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class':'stripe'})
print(table.prettify())
# soup = BeautifulSoup(html)
# table = soup.find('table', attrs={'class': 'resultsTable'})
#
# list_of_rows = []
# for row in table.findAll('tr')[1:]:
#     list_of_cells = []
#     for cell in row.findAll('td'):
#         text = cell.text.replace('&nbsp;', '')
#         list_of_cells.append(text)
#     list_of_rows.append(list_of_cells)
#
# outfile = open("./inmates.csv", "wb")
# writer = csv.writer(outfile)
# writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
# writer.writerows(list_of_rows)
