class Solution:
    def binarySearch(self, arr, element):
        left = 0
        right = len(arr) - 1
        return self.search(arr, left, right, element)

    def search(self, arr, left, right, element):
        if(right < left):
            return -1
        mid = int((left + right) / 2)
        if(arr[mid] == element):
            return mid
        if(arr[mid] < element):
            return self.search(arr, mid, right, element)
        else:
            return self.search(arr, left, mid, element)


solution = Solution()
print(solution.binarySearch([2, 4, 5, 8, 12, 16, 29, 30], 16))
