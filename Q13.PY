 
def divisible_prefix(arr, k):
    running_sum = 0
    k = abs(k)

    for value in arr:
        running_sum += value

        if running_sum % k == 0:
            return True

    return False

n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    value = int(input("Enter an element: "))
    arr.append(value)

k = int(input("Enter k (non-zero): "))

print("Result:", divisible_prefix(arr, k))