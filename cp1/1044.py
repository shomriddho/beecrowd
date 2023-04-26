a = None
b = None
list = None


list = input().split(" ")
a = int (list[0])
b = int (list[1])

if a % b == 0 or b % a == 0:
    print("Sao Multiplo cs")
else:
    print("Nao sao Multiplos")  