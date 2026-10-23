
arr_input = input("Enter integers separated by commas: ")

arr = []

for value in arr_input.split(","):
    arr.append(int(value.strip()))

smallest = arr[0]

for num in arr:
    if abs(num) < abs(smallest):
        smallest = num

print(smallest)

