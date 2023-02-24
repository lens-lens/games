from random import randint 

dice_sides = 6
throw_result = randint(1, dice_sides)

print('The number is: ')

for i in range(6):
    throw_result = randint(1, dice_sides)
    print('The number is: ')
    print(throw_result)
    input()
   

#TODO history of throw numbers