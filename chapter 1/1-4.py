def areAnagram1(str1, str2):
    if len(str1) != len(str2):
        return False
    chars = []
    for i in range(256):
        chars.append(0)
    for c in str1:
        chars[ord(c)] += 1
    for c in str2:
        chars[ord(c)] -= 1
    for i in range(len(chars)):
        if(chars[i] != 0):
            return False
    return True


def areAnagram2(str1, str2):

    return sorted(str1) == sorted(str2)


print(areAnagram2('salam', 'maals'))
