# https://pythonprinciples.com/challenges/Online-status/

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(x):
    value = []
    for i in x.values():
        if i == "online":
            value.append(i)
        else:
            pass
    return(len(value))

x = statuses
print(online_count(x))