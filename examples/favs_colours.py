#TODO: uzytkownik zgaduje 3 ulubione kolory Milenki i dostaje odpowiedź, który to w kolejności
"""
input: słownik kolorów z przypisaną wartością 1-3
output: wartość trafionego koloru 1-3 lub info, ze ten kolor nie zalicza się
"""

"""
program zgadywanka kolorow:
    input -> None
    output -> jak zgadniesz wszystkie -> print "super koniec"

body:
    0.0 Kolekcja ulubionych kolorow milenki
    0.1 Lista odgadniętych kolorow = []
    1. pętla pytająca o kolory:
        a. color = zapytaj o kolor    
        b. sprawdz czy kolor lubi Milenka
            i. jesli tak: 
                print pozycja w rankingu Milenki 
                dopisz kolor do listy odgadnietych kolorow (.append(color))
                i powtórz wybór koloru az zgadniesz 3
                jesli masz juz 3 kolory przerwij petle (break)
            j. jeśli nie: print nie i powtórz wybór kolorów
"""




milenkas_favs_colours = {'pink':1, 'violet':2, 'green':3}

your_choice = input("Which one of 3 favs Milenka's colours is: ")
print(milenkas_favs_colours.get(your_choice, f"{your_choice} isn't"))