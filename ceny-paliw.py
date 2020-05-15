# -- coding: utf-8 --
from bs4 import BeautifulSoup  # scrapper witryn
import requests
from datetime import datetime
from prettytable import PrettyTable  # do stworzenia tabelki html
import csv
import os
import time
import operator #do sortowania

# kod startujacy moduł bs4
page = requests.get('https://www.wnp.pl/nafta/ceny_paliw/')

soup = BeautifulSoup(page.text, 'html.parser')
soup.encode("utf-8")

# zmienne
data = []
headers = []

data1 = soup.select('div', class_='box-')
tabelka = soup.find('table', class_='table-3')

# znajdowanie daty
datka = soup.find_all("div", {"class": "box-8"})[2].text
datka2 = str(datka)[-11:-1]

dzisiejsza_data = datetime.today()
data_aktualizacji_cen = datetime.strptime(datka2, '%Y-%m-%d')
roznica_dat = (dzisiejsza_data - data_aktualizacji_cen).days
roznica_string = '\n Ostatnia aktualziacja cen : {} dni temu'.format(
    roznica_dat)

# parsowanie nagłowka tabeli
rows = tabelka.find_all('tr')
header = tabelka.find_all('th')
for th in header:
    headers.append(th.a.text)

# parsowanie tablki z cenami
for rows in rows:
    cols = rows.find_all('td')
    # dodaje do listy jesli element nie jest pusty
    cols = [ele.text.strip() for ele in cols]
    data.append([ele.replace(u'\xa0\xa0', u' ') for ele in cols if ele])

# zmiana cen na typ float
topdata = []
for listki in data:
    nowadata = []
    for element in listki:
        
        if element != listki[0]:

            cena = element
            cenakropka = cena[0] + "." + cena[2:]
            cenafloat = float(cenakropka[:4])
            
            
            
            nowadata.append(cenafloat)
        
        else:
            nowadata.append(element)
    topdata.append(nowadata)


#lista z wojewodztwami
wojewodztwa = []
for i in data[1:]:
    wojewodztwa.append(i[0])



# zapisywanie do pliku html
def dodawniezl(topdata):
    dataE = []
    for listki in topdata[1:]:
        datab =[]
        for element in listki:
            if element != listki[0]:
                datab.append("{:.2f}".format(element) + " zl")
            else:
                datab.append(element)
        dataE.append(datab)
    return dataE

def zapis_html(data):
   
    x = PrettyTable(headers)
    x.format = True
    for i in data[1:]:
        x.add_row(i)

    with open("ceny-paliw.html", "w", encoding='utf-8') as file:
        modyfikacja = time.ctime(os.path.getmtime(
            'ceny-paliw.html'))  # data modyfikacji pliku

        file.write(roznica_string + '( {} )'.format(datka2) +
                   'na stronie https://www.wnp.pl/nafta/ceny_paliw/')
        file.write(x.get_html_string())
        file.write('Plik zmodyfikowano : ' + str(modyfikacja) + '\n')


# zapis do csv

def zapis_csv(data, headers):
    with open('output.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        data.insert(1, headers)
        writer.writerows(data)


def kalkulator_tankowania(data):
    while True:
        try:
            ilosc = float(input('Podaj ile litrow chcesz zatankowac: \t'))
            while True:
                paliwo = int(input('''
                            1 ON
                            2 E95
                            3 S98
                            4 LPG \n
                            Podaj numer paliwa:  '''))
                if paliwo not in range(1, 5):
                    print(" musisz podać liczbe miedzy 1 a 4")
                    continue
                else:
                    break

        except ValueError:
            print("Musisz podac odpowiednia liczbe")
            continue
        else:
            break
    while True:
        region = input('Wprowadz poprawną nazwe regionu z zakresu:  ' + " ".join(wojewodztwa) + '\t')
        if region.capitalize() in wojewodztwa:
            break
        else:
            print('podałes nieprawidłowy region  ' + " ".join(wojewodztwa))
            continue

    for listki in data:
        for element in listki:
            if element == region.capitalize():

                cena = listki[paliwo]
    x = PrettyTable()
    x.field_names = ['województwo', 'rodzaj paliwa','ilość litrów', 'cena za litr', 'do zapłaty']
    x.add_row([region, headers[paliwo], ilosc, cena, ilosc*cena])
    print(x)
    
# uzytkownik wybiera czy chce plik html czy csv



    


    
def posortowane():
    while True:
        try:
            paliwo = int(input('''
                                1 ON
                                2 E95
                                3 S98
                                4 LPG \n
                                Podaj numer paliwa:  '''))
            if paliwo not in range(1, 5):
                print("musisz podać liczbe miedzy 1 a 4")
                continue
            
        except ValueError:
            print(' musisz podać liczbe pomiedzy 1 a 4') 
        else:
            break
    del topdata[0]
    topdata_posortowane = sorted(dodawniezl(topdata), key = operator.itemgetter(paliwo), reverse=True)

    x = PrettyTable()
    x.field_names = headers
    for i in topdata_posortowane:
        x.add_row(i)
    print(x)
    
    



while True:

    user_choice = input("""Wybierz numer :
                        1. Kalkulator ceny paliwa
                        2. Sortowanie według ceny
                        3. Stworz plik csv
                        4. Stworz plik html
                        5. wyjdz \n""")

    if user_choice not in ['1', '2', '3', '4', '5']:
        print('wprowadziles zly numer, wybierz 1-5')
        continue
    elif user_choice == "1":
        kalkulator_tankowania(topdata)
        break
    elif user_choice == "2":
        posortowane()
        break
    elif user_choice == "3":
        zapis_csv(dodawniezl(topdata), headers)
        break
    elif user_choice == "4":
        zapis_html(dodawniezl(topdata))
        break
    elif user_choice == "5":
        break
