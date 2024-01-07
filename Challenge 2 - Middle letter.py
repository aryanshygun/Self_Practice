
def mid(x):
    middle = []
    if len(x) % 2 != 0 :
        y = int((len(x)-1)/2)
        name_middle = x[y]
        middle.append(name_middle)
    else:
        name_middle = ""
        middle.append(name_middle)
    for i in middle:
        return(i)


x = input(" type your name\n")
print(mid(x))