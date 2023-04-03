'''
input: 
    1) pusta plansza
    2) ruch uzytkownika x
    3) ruch uzytkownika y
    4) powtarzanie ruchów wypełniając puste pola
    5) warunki:
        - brak mozliwosci nadpisywania ruchow drugiego gracza
        - zakończenie gry po trzech polach wypełnionych zgodnie z zasadami
        - zakończenie gry po 9 ruchach
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
for field in game_field:
    print(field)

#TODO 4: zapętlenie ruchów
move = 0

def player_move(sign:str) -> bool:
    x, y = map(int, input('Wybierz pole od 0 0 do 2 2: ').split())
    print(f'Your x is {x} and your y is {y}')
    if game_field[x][y] == '':
        game_field[x][y] = 'x'
    else:
        print('This field is not empty')
        return False

    for field in game_field:
        print(field)
    return True

while move < 9:
    move += 1
    player = 'x'
    is_even = move%2
    if is_even == 0:
        player = 'o'

    ok = player_move(player)
    if ok is not True:
        break


#TODO 2: ruch uzytkownika x
#     x, y = map(int, input('Wybierz pole od 0 0 do 2 2: ').split())
#     print(f'Your x is {x} and your y is {y}')
#     if game_field[x][y] == '':
#         game_field[x][y] = 'x'
#     else:
#         print('This field is not empty')
#         break

#     for field in game_field:
#         print(field)

# #TODO 3: ruch uzytkownika o
#     x2, y2 = map(int, input('Wybierz pole od 0 0 do 2 2: ').split())
#     print(f'Your x is {x} and your y is {y}')
#     if game_field[x2][y2] == '':
#         game_field[x2][y2] = 'o'
#     else:
#         print('This field is not empty')
#         break

#     for field in game_field:
#         print(field)