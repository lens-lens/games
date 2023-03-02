import random

#TODO: uzytkownik wybiera psa na spacer, losując numer przypisany do imienia w liście:
"""
input: lista imion psów
output: losowe imię 1-go psa z listy
>stworzyć listę imion
>stworzyć funkcję 
>zwrócić 1-no losowe imię z listy
"""

names_list = ('Pimpek', 'Reksio', 'Scooby')

def dogs_name(name) -> str:
    return name

random_name_from_list = dogs_name(names_list)
print('Your dog for walk today is',random.choice(random_name_from_list))