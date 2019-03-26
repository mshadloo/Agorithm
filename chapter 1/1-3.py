def removeDuplicate1(str):
    checker = 0
    i = 0
    while i < len(str):
        intVal = ord(str[i]) - ord('a')
        if (checker & (1 << intVal) > 0):
            str = str[:i] + str[i + 1:];
        else:
            checker |= (1 << intVal)
            i += 1

    return str


def removeDuplicate2(str):
    str = ''.join(sorted(str))
    i = 1
    while(i < len(str)):
        if(str[i] == str[i - 1]):
            str = str[:i] + str[i + 1:];
        else:
            i = i + 1
    return str


def removeDuplicate3(str):

    return "".join(set(str))


print('str=' + removeDuplicate2('aaaaabbbbbb'))
