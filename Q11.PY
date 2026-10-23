

MOD = 10**9 + 7

def modular_addition(arr):
    result = 0

    for value in arr:
        result = (result + value) % MOD

    return result

n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    value = int(input("Enter an element: "))
    arr.append(value)

print("Result:", modular_addition(arr))

