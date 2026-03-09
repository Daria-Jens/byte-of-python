# solution chapter exception task 4
# запитання, розділ «Винятки», завдання 4
def отримати_колір(рядок,стовпець):
    try:
        r=int(рядок)
        c=int(cтовпець)
    except ValueError:
        return "введено не числа"
    if (c < 0) or (c>7) or (r<0) or (r>7):
        return "некоректний індекс"
    return шахова_дошка[r][c]
