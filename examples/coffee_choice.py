#TODO: uzytkownik wybiera kawę z mlekiem albo bez:
"""
input: mozliwe kawy w kawiarni
output: wybór kawy przez uytkownika
>if, else -> bool
>zwrócić True or False
"""

input('Choose coffe: with milk or without milk: ')
with_milk = False
without_milk = True

def what_coffe_you_choose(coffe_choice) -> bool:
    if coffe_choice is with_milk:
        return False
    else: 
        return True
    
choosen_coffee_with = what_coffe_you_choose(coffe_choice=with_milk)
print('You order coffee', choosen_coffee_with)

choosen_coffee_without = what_coffe_you_choose(coffe_choice=without_milk)
print('You order coffee', choosen_coffee_without)