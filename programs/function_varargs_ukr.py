def підсумок(a=5, *номера, **телефонна_книга):
    print('a', a)
    
    #прохід по всіх елементах кортежу
    for один_елемент in номера:
        print('один_елемент', один_елемент)
        
    #прохід по всіх елементах словника  
    for перша_частина, друга_частина in телефонна_книга.items():
        print(перша_частина,друга_частина)

підсумок(10,1,2,3,Джек=1123,Джон=2231,Інге=1560)
