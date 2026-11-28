
def minimum_subarray_sum(arr):
    min_sum = arr[0]

    for i in range(len(arr)):
        current_sum = 0

        for j in range(i, len(arr)):
            current_sum += arr[j]

            if current_sum < min_sum:
                min_sum = current_sum

    return min_sum

n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

result = minimum_subarray_sum(arr)

print("Minimum Subarray Sum:", result)