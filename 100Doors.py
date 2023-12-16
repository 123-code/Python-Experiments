

def Doors():
    # initial state
    doors = [False]*101

    for x in range(1,101):
       

        for j in range(x,101,x):
            doors[j] = not doors[j]

    for i in range(1,101):

        if  doors[i] is True:
            print(i,end=",")




if __name__ == "__main__":
    Doors() 

'''
doors = [False] * 101
print(doors)

# for each door, flip its state 
for x in range(1,101):
    doors[x] = not doors[x]

print(doors)


for i in range(1,6):
    for j in range(1,4):
        print(i,j)

for i in range(1,10,2):
    print(i)



'''