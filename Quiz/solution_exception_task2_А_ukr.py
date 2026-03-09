# solution chapter exception task 2 variant A
# розв’язання з розділу «Винятки», завдання 2 варіант А
while True:
    print("будь ласка, введіть рік вашого народження у форматі YYYY")
    рік_текст = input(">>>")
    try:
        рік = int(рік_текст)
    except ValueError:
        print("введено не число, будь ласка, спробуйте ще раз")
        continue
    # введення було правильним
    break
print("у 2050 році вам буде ", 2050-рік, "років")  

