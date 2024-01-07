# https://pythonprinciples.com/challenges/Capital-indexes/

def capital_indexes(str):
    chars=[]
    for num,letter in enumerate(str):
        if letter.isupper():
            chars.append(num)

    return(chars)
print(capital_indexes(input("type a string\n")))