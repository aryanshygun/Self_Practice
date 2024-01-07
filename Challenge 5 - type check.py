# https://pythonprinciples.com/challenges/Type-check/
def only_ints(x,y):
    if type(x) is int and type(y) is int:
        answer = True
    else:
        answer = False
    return(answer)

#def only_ints(a, b):
#    return type(a) == int and type(b) == int

x,y = 2,"hello"
print(only_ints(x,y))