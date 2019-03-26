class Solution:
    def groupAnagrams(self, arr):
        angaramsHash = {}
        for s in arr:
            s_s = ''.join(sorted(s))
            if(angaramsHash.get(s_s) is None):
                angaramsHash[s_s] = [s]
            else:
                angaramsHash[s_s].append(s)
        keySets = angaramsHash.keys()
        i = 0
        for key in keySets:
            angaramsHash[key].sort()
            s = angaramsHash[key][0]
            angaramsHash[s] = angaramsHash.pop(key)
        for key in sorted(angaramsHash.keys()):
            for s in angaramsHash[key]:
                arr[i] = s
                i += 1


solution = Solution()
arr = ['abcdd', 'cddba', 'mjfh', 'haha', 'ahah']
solution.groupAnagrams(arr)
print(arr)
