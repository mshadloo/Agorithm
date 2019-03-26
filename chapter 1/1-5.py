def replaceSpace(str):
    i = 0
    while(i < len(str)):
        if(str[i] == ' '):
            str = str[:i] + '%20' + str[i + 1:]
            i += 2
        else:
            i += 1
    return str


print(replaceSpace('ha ha ha'))
