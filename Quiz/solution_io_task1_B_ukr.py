# solution chapter IO task 1 variant B
text = "Hello World!"
with open("hello.txt", "w") as myfile:
    myfile.write(text)
# закривається автоматично!
print("Файл було записано на диск")
