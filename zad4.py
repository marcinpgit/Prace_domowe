# program znajdujący wartośći, które występują tylko raz

lista_a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

print(lista_a)

for i in lista_a:
    print(i)
    if lista_a.count(i) == 1:
        print("Element ", i, " występuje na liście tylko raz.")