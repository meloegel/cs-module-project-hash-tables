def no_dups(s):
    nonDups = []
    if s == '':
        return ''
    x = s.split(' ')
    a = dict.fromkeys(x)
    for key in a.keys():
        nonDups.append(key)
    return ' '.join(nonDups)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))