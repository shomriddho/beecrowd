name = input()
salary = float(input())
sold = float(input())
bonus = float(sold * (15/100))
total = salary + bonus
print(f'TOTAL = R$ {total:.2f}')
