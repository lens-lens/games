import random

def draw_task():
    numbers = [1, 2, 3, 4, 5, 6]
    random.shuffle(numbers)
    return numbers

print(draw_task())