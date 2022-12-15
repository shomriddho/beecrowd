line1 = input().split(" ")
line2 = input().split(" ")
num1, flot1, nam1 = line1
num2, flot2, nam2 = line2
total = (int(flot1) * float(nam1)) + (int(flot2) * float(nam2))# exp: input :
"""
3 4 5
1 2 3
output: 4*5=20+2*3=26.00
"""
print(f'VALOR A PAGAR: R$ {total:.2f}')
