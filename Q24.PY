
def shortest_subarray(arr, target):
    min_length = len(arr) + 1

    for i in range(len(arr)):
        current_sum = 0

        for j in range(i, len(arr)):
            current_sum += arr[j]

            if current_sum >= target:
                length = j - i + 1

                if length < min_length:
                    min_length = length

                break

    if min_length == len(arr) + 1:
        return 0

    return min_length

n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

target = int(input("Enter target: "))

result = shortest_subarray(arr, target)

print("Shortest Subarray Length:", result)