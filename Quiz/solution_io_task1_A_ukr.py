text = "Привіт,Світ!"
myfile = open("hello.txt", "w") # режим запису
myfile.write(text)
myfile.close()
print("Файл було записано на диск")
