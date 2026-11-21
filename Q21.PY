
arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target value: "))

index = -1

for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break

if index != -1:
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr.pop()

print("Updated array:", arr)
