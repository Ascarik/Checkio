num1 = int(input("студенты: "))
num2 = int(input("яблоки: "))
t = num2 % num1
print("Яблок у студентов: {}, в корзине: {}".format((num2 - t) // num1, t))
