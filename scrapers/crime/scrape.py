import csv
import xlwt
from xlwt import Workbook
import requests
from bs4 import BeautifulSoup

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content
# print(html)

soup = BeautifulSoup(html,features="html.parser")
table = soup.find('tbody', attrs={'class':'stripe'})

listOfRows = []
for row in table.findAll('tr'):
    ListOfNames = []
    first = row.find('td', attrs = {'data-th': 'First Name'})
    last = row.find('td', attrs = {'data-th': 'Last Name'})
    try:
        # print(first.get_text() + ", " + last.get_text())
        ListOfNames.append(first)
        ListOfNames.append(last)
    except Exception as e:
        print("########################")
        print("an error has occured")
        print("########################")
    listOfRows.append(ListOfNames)

outFile = open("./myInmates.csv","wb")
writer = csv.writer(outFile)
writer.writerows(listOfRows)




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
