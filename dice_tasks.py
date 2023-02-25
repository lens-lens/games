import random

#TODO PSEUDOKOD - szczegółowe krok po kroku to do:
"""
funkcja 
    input nic
    output list intow od 1 do 6 w losowej kolejnosci

    > a <- lista od 1 do 6
    > b <- pomieszana list a
    > zwróć b
"""

#TODO KOD - prawidłowy kod na podstawie pseudokodu:
def draw_task():
    numbers = [1, 2, 3, 4, 5, 6]
    random.shuffle(numbers)
    return numbers

print(draw_task())