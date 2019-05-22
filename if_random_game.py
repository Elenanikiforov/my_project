import random
x=random.randint(1,4)
y=int(input("Введите число от 1 до 4:\n"))
if x==y:
    print("Победа!\n")
elif x>y:
    print("Рез-т больше введенного числа\n")
elif x<y:
    print("Рез-т меньше введенного числа\n")
