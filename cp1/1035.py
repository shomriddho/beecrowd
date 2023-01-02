a, b, c, d = map(int, input().split())

if ((b > c) & (d > a )& ((c+d) > (a+b)) & (c >= 0) & (d >= 0) & (a % 2 == 0)):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")


2+3*5+1