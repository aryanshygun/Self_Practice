x = 5
y = 5
for i in range(x):
    for j in range(y):
        if i==0 or i==x-1 or j==0 or j==y-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    
print("\n")
    
for i in range(y):
    for j in range(y):
        print("*", end=" ")
    print()
    
    
print("\n")

for i in range(x):
    for j in range(y):
        if (i+j)%2 == 0:
            print("-", end=" ")
        else:
            print("I", end=" ")
    print()
    

    
    
    
    
    
    
    
    
    