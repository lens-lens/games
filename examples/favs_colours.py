#TODO: uzytkownik zgaduje 3 ulubione kolory Milenki i dostaje odpowiedź, który to w kolejności
"""
input: słownik kolorów z przypisaną wartością 1-3
output: wartość trafionego koloru 1-3 lub info, ze ten kolor nie zalicza się
"""

milenkas_favs_colours = {'pink':1, 'violet':2, 'green':3}

your_choice = input("Which one of 3 favs Milenka's colours is: ")
print(milenkas_favs_colours.get(your_choice, f"{your_choice} isn't"))