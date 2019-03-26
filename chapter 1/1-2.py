def reverseString(str):
    str_list = list(str[0:len(str) - 1])
    str_list.reverse()
    return ''.join(str_list)


str = 'salam'
print(reverseString('salam'))
