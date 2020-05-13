# python-srednie-ceny-paliw
Pierwszy mój program w pythonie pisany w celach edukacyjnych, wiem kod wygląda koszmarnie,


Funkcje programu:
1. Program pobiera ceny paliwa ze strony "https://www.wnp.pl/nafta/ceny_paliw/"
2. Zapisuje je albo do pliku html lub pliku csv wedle wyboru użytkownika
3. Pobiera date ostatniej aktualizacji cen i pokazuje w pliku html ile dni mineło od ostatniej aktualizacji
4. Pokazuje date ostatniej modyfikacji pliku html
5. kalkulator ceny po podaniu ile litrów chcemy zatankować + dodane 'zabezpieczenie' w przypadku niepoprawnych danych wprowadzonych przez usera w input

Wykorzystane biblioteki:
os, BeautifulSoup, requests, datetime, prettytable, csv, time


TO-DO list.
- sortowanie danych według ceny lub województwa
- 
- tworzenie nowych plików z cenami lub dopisywanie aktualnych cen do starych plików z cenami według daty
- obliczenie zmian cen i tworzenie wykresów
- napisanie GUI
