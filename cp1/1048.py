Salary = float(input())

earned = 0.0

if (Salary >= 0 and Salary <= 400):
    earned = Salary * (15.0/100)
    print("Novo salario: {:.2f}".format((earned + Salary)))
    print("Reajuste ganho: {:.2f}".format(earned))
    print("Em percentual: 15 %")

elif (Salary > 400 and Salary <= 800):
    earned = Salary * (12.0/100)
    print("Novo salario: {:.2f}".format((earned + Salary)))
    print("Reajuste ganho: {:.2f}".format(earned))
    print("Em percentual: 12 %")

elif (Salary > 800 and Salary <= 1200):
    earned = Salary * (10.0/100)
    print("Novo salario: {:.2f}".format((earned + Salary)))
    print("Reajuste ganho: {:.2f}".format(earned))
    print("Em percentual: 10 %")

elif (Salary > 1200 and Salary <= 2000):
    earned = Salary * (7.0/100)
    print("Novo salario: {:.2f}".format((earned + Salary)))
    print("Reajuste ganho: {:.2f}".format(earned))
    print("Em percentual: 7 %")
    
else:
    earned = Salary * (4.0/100)
    print("Novo salario: {:.2f}".format((earned + Salary)))
    print("Reajuste ganho: {:.2f}".format(earned))
    print("Em percentual: 4 %")

"""
salary = 400
earned = 400 * (15/100)
               =0.15
400 * 0.15
=60

1000
earned = 1000 * (10/100)
                =

"""