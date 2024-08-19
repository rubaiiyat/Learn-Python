myList = [2, 3, 4, 5, 6]


for list in myList:
    cube = (lambda x: x**3)(list)
    print(cube)
