# solution chapter IO task 2 variant A
# розв’язання з розділу "введення-виведення" Завдання 2 варіант А 
текст = "\n\n\nЯк справи??\n"
with open("hello.txt", "a") as мій_файл:
    мій_файл.write(текст)
print("Текстовий рядок додано")
