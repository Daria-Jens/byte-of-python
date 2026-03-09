# solution chapter IO task 3 variant A
# розв’язання з розділу "введення-виведення" Завдання 3 варіант А 
with open("hello.txt") as myfile:
    lines = myfile.readlines()
print("знайдено рядків:", len(lines))
