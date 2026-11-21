
arr = list(map(int, input("Enter array elements: ").split()))

total = 0

for i in range(len(arr) - 1, -1, -1):
    current = arr[i]
    arr[i] = total
    total = total + current

print("Suffix sum:", arr)
