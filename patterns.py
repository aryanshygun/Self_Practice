# row = 10

# for i in range(0,row):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

# print("\n")
# print("\n")
# print("\n")
# print("\n")

# for j in range(1,row+1):
#     print("* "*j)

row = 10
k = 2 * row -2

for i in range(row,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k = k+1
    for j in range(0,i+1):
        print("*", end=" ")
    print(" ")