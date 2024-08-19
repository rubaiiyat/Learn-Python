mytuple = (1, 2, 3, 4, 5)

print(mytuple[0])

if 6 in mytuple:
    print("Exist")
else:
    print("Not")


tpl1, tpl2, tpl3, *others = mytuple

print(tpl1, tpl2, tpl3, others)

mytuple = ((1, 2, 3), ("apple", "mango", "pineapple"), (True, False))
print(mytuple[0][1])
print(mytuple[1][0])
print(mytuple[2][1])
