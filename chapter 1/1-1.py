# def hasUniqueCharacter(str):
#     chars = []
#     for i in range(256):
#         chars.append(0)
#     for c in range(len(str)):
#         if (chars[ord(str[c])] == 0):
#             chars[ord(str[c])] += 1
#         else:
#             return false
#     return true


def hasUniqueCharacter1(str):
    chars = []
    for i in range(256):
        chars.append(0)
    for c in str:
        if (chars[ord(c)] == 0):
            chars[ord(c)] += 1
        else:
            return false
    return true


def hasUniqueCharacter2(str):
    sorted_str = sorted(str)
    for i in range(1, len(sorted_str)):
        if(sorted_str[i] == sorted_str[i - 1]):
            return False
    return True


def hasUniqueCharacter3(str):
    checker = 0
    for c in str:
        intValue = ord(c) - ord('a')
        if ((checker & (1 << intValue)) > 0):
            return False
        checker = checker | (1 << intValue)
    return True


str = 'bcd'
print(hasUniqueCharacter3(str))
