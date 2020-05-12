 # -- coding: utf-8 --
from bs4 import BeautifulSoup #scrapper witryn
import requests
from datetime import datetime
from prettytable import PrettyTable # do stworzenia tabelki html
import csv
import os, time

#kod startujacy moduł bs4
page = requests.get('https://www.wnp.pl/nafta/ceny_paliw/')

soup = BeautifulSoup(page.text, 'html.parser')
soup.encode("utf-8")

#zmienne
data = []
headers =[]

data1 = soup.select('div', class_='box-')
tabelka = soup.find('table', class_='table-3')

#znajdowanie daty
datka = soup.find_all("div", {"class" : "box-8"})[2].text
datka2 = str(datka)[-11:-1]

dzisiejsza_data = datetime.today()
data_aktualizacji_cen = datetime.strptime(datka2, '%Y-%m-%d')
roznica_dat = (dzisiejsza_data - data_aktualizacji_cen).days
roznica_string = '\n Ostatnia aktualziacja cen : {} dni temu'.format(roznica_dat)





#parsowanie nagłowka tabeli
rows = tabelka.find_all('tr')
header = tabelka.find_all('th')
for th in header:
    headers.append(th.a.text)

#parsowanie tablki z cenami
for rows in rows:
    cols = rows.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele.replace(u'\xa0\xa0', u' ') for ele in cols if ele]) #dodaje do listy jesli element nie jest pusty

pod_csv = [headers, data]
#zapisywanie do pliku html
def zapis_html():
    
    x = PrettyTable(headers)
    x.format = True
    for i in data[1:]:
        x.add_row(i)
    
    with open("ceny-paliw.html", "w", encoding='utf-8') as file:
        modyfikacja = time.ctime(os.path.getmtime('ceny-paliw.html')) #data modyfikacji pliku
        
        file.write(roznica_string + '( {} )'.format(datka2) + 'na stronie https://www.wnp.pl/nafta/ceny_paliw/')
        file.write(x.get_html_string())
        file.write('Plik zmodyfikowano : ' + str(modyfikacja) + '\n')

        
#zapis do csv
 
def zapis_csv(data, headers):
    with open('output.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        data.insert(1, headers)
        writer.writerows(data)


#uzytkownik wybiera czy chce plik html czy csv

while True:
   
    user_choice = input("""Wybierz numer :
                        1. Stworz plik html
                        2. Stworz plik csv
                        3. wyjdz \n""")
    
    if user_choice not in ['1', '2', '3']:
        print('wprowadziles zly numer, wybierz 1-3')
        continue
    elif (user_choice) == "1":
        zapis_html()
        break
    elif user_choice == "2":
        zapis_csv(data, headers)
        break
    elif user_choice == "3":
        break
    
        
     
