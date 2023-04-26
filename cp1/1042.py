line = list(map(int,input().split(' ')))

org = line.copy()

line.sort()

for i in line:
    print(i)

print()
for j in org:
    print(j)
