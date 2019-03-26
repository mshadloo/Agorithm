arr = [-2, -3, 4, -1, -2, -1, 5, -3, 8]

first_index = 0
end_index = 0

s = 0
best = 0
for i in range(1, len(arr)):
    s = s + arr[i]
    if(s > 0):
        best = best + s
        end_index = i
    if(arr[i] >= best):
        best = arr[i]
        s = 0
        first_index = i
        end_index = 0


print(first_index)
print(end_index)
print(best)
