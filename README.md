# python-srednie-ceny-paliw
Pierwszy mój program w pythonie pisany w celach edukacyjnych, wiem kod wygląda koszmarnie,


Funkcje programu:
1. Program pobiera ceny paliwa ze strony "https://www.wnp.pl/nafta/ceny_paliw/"
2. Sortowanie województw według ceny wybranego paliwa
3. Kalkulator tankowania: użytkownik podaje ilośc litrów, region, rodzaj paliwa, program liczy cene do zapłaty
4. Zapisuje je albo do pliku html lub pliku csv wedle wyboru użytkownika
5. Pobiera date ostatniej aktualizacji cen i pokazuje w pliku html ile dni mineło od ostatniej aktualizacji
6. Pokazuje date ostatniej modyfikacji pliku html


Wykorzystane biblioteki:
os, BeautifulSoup, requests, datetime, prettytable, csv, time


TO-DO list. 
- tworzenie nowych plików z cenami lub dopisywanie aktualnych cen do starych plików z cenami według daty
- obliczenie zmian cen i tworzenie wykresów
- napisanie GUI

#SCREENSHOTY
![Test Image 1](https://i.imgur.com/vny53vk.png)
