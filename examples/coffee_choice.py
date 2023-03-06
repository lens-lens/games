#TODO: uzytkownik wybiera kawę z mlekiem albo bez:
"""
input: mozliwe kawy w kawiarni
output: wybór kawy przez uytkownika
>if, else -> bool
>zwrócić True or False
"""

user_choice = input('Choose coffe: with milk or without milk: ')

def is_coffe_without_milk(coffe_choice: bool) -> bool:
    if coffe_choice == "with milk":
        return False
    elif coffe_choice == "without milk":
        return True
    else:
        print("write 'with milk' or 'without milk'")

coffe_without_milk = is_coffe_without_milk(coffe_choice=user_choice)
print('Your coffee will be without milk:', coffe_without_milk)

# choosen_coffee_with = what_coffe_you_choose(coffe_choice=with_milk)
# print('You order coffee', choosen_coffee_with)

# choosen_coffee_without = what_coffe_you_choose(coffe_choice=without_milk)
# print('You order coffee', choosen_coffee_without)