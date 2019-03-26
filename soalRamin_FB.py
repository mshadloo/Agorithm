# finding shortest substring containing all letters of alphabet!


def find(s, alphabet):
    hashTable = {el: 1000 for el in alphabet}
    print(hashTable)
    firstChar = s[0]
    first_ind = 0
    hashTable[firstChar] = 0
    i = 1
    seenSofar = 1
    short_sub = s
    for i in range(len(s)):
        c = s[i]
        if(hashTable[c] == 1000):

            hashTable[c] = i
            seenSofar += 1

        else:
            hashTable[c] = i
            firstChar, first_ind = update(hashTable)
        if(seenSofar == len(alphabet)):

            if(i - first_ind + 1 < len(short_sub)):
                short_sub = s[first_ind:i + 1]
    return short_sub


def update(hashTable):
    min_ind = 1000
    firstchar = ''
    for e in hashTable.keys():
        if(hashTable[e] < min_ind):
            min_ind = hashTable[e]
            firstchar = e
    return firstchar, min_ind


def getShortestSubstr(s,alphabet):
    hashTable = {el: 0 for el in alphabet}
    seenSofar=0;
    start=0
    short_substr=s
    for i in range(len(s)):
        c=s[i]
        if(hashTable[c]==0):
            seenSofar +=1
        hashTable[c] +=1
        if(seenSofar==len(alphabet)):
            while (start<i and hashTable[s[start]]>1 ):
                hashTable[s[start]]-=1
                start +=1;
            if(i-start+1<len(short_substr)):
                short_substr=s[start:i+1]
    return short_substr




alphabet={'a','b','c','d','e'}
s="aaabbacdcceab"
print(getShortestSubstr(s,alphabet))
