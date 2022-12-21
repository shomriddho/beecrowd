A=float(input())
N=A
a=N/100
b=N%100
c=b/50
d=b%50
e=d/20
f=d%20
g=f/10
h=f%10
i=h/5
j=h%5
k=j/2
l=j%2

E=A*100
B=(int(E))
m=B%100
n=m/50
o=m%50
p=o/25
q=o%25
r=q/10
s=q%10
t=s/5
u=s%5
print("NOTAS:")
print(f"{int(a)} nota(s) de R$ 100.00")
print(f"{int(c)} nota(s) de R$ 50.00")
print(f"{int(e)} nota(s) de R$ 20.00")
print(f"{int(g)} nota(s) de R$ 10.00")
print(f"{int(i)} nota(s) de R$ 5.00")
print(f"{int(k)} nota(s) de R$ 2.00")
print(f"MOEDAS:")
print(f"{int(l)} moeda(s) de R$ 1.00")
print(f"{int(n)} moeda(s) de R$ 0.50")
print(f"{int(p)} moeda(s) de R$ 0.25")
print(f"{int(r)} moeda(s) de R$ 0.10")
print(f"{int(t)} moeda(s) de R$ 0.05")
print(f"{int(u)} moeda(s) de R$ 0.01")