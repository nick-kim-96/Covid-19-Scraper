import requests,datetime
from bs4 import BeautifulSoup

def scrapeGlobalCase ():
    try:
        url = "https://www.worldometers.info/coronavirus/usa/california/" #Getting data from this URL
        req = requests.get(url)
        bsObj = BeautifulSoup(req.text, "html.parser")
        bigData = bsObj.find_all("div",class_ = "maincounter-number")

        table = bsObj.find('table', id="usa_table_countries_today") #Specific table data
        rows = table.find_all('tr')

        data = []
        for row in rows: #For every row in the table
            cols = row.find_all('td')
            data.append(cols)

        cities = []
        cases = []
        i = 2
        total = 0
        while i < len(data) - 5: #Taking out unneccessary information
            total += int(data[i][1].contents[0].replace(',', ''))
            cities.append(str(data[i][0].contents[0].replace(',', '')).strip('\n'))
            cases.append(int(data[i][1].contents[0].replace(',', '')))
            i+=1
        TimeNow = datetime.datetime.now() 

        return { #Object returns date, total, list of cities, list of cases
            'date': str(TimeNow),
            'total': str(total),
            'cities': cities,
            'cases': cases,
        }
        
    except Exception as e: print(e)
