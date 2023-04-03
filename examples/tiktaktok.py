'''
input: 
    1) pusta plansza
    2) ruch uzytkownika x
    3) ruch uzytkownika y
    4) warunek zakończenia gry
    5) powtarzanie ruchów wypełniając puste pola
    6) przerwanie gry po osiągnięciu warunku
output: stan gry, az do spełnienia warunku i zakończenia
'''
#TODO 1: pusta plansza
field_00 = ''
field_01 = ''
field_02 = ''

field_10 = ''
field_11 = ''
field_12 = ''

field_20 = ''
field_21 = ''
field_22 = ''

level_1 = [field_00, field_01, field_02]
level_2 = [field_10, field_11, field_12]
level_3 = [field_20, field_21, field_22]

game_field = [level_1, level_2, level_3]
# print(game_field)
for level in game_field:
    print(level)

#TODO 2: ruch uzytkownika
x, y = map(int, input('Wybierz pole od 0 0 do 2 2: ').split())
print(f'Your x is {x} and your y is {y}')
game_field[x][y] = 'x'
# print(game_field)
for level in game_field:
    print(level)

#TODO 3: kolejne ruchy

