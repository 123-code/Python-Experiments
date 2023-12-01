doors = [False] * 101
print(doors)
for x in range(1,101):
    doors[x] = not doors[x]

print(doors)


for i in range(1,6):
    for j in range(1,4):
        print(i,j)

for i in range(1,11,2):
    print(i)