
def closest_pair(temps, target):
    left = 0
    right = len(temps) - 1

    min_diff = float('inf')
    result = (temps[left], temps[right])

    while left < right:
        current_sum = temps[left] + temps[right]
        diff = abs(current_sum - target)

        if diff < min_diff:
            min_diff = diff
            result = (temps[left], temps[right])

        if current_sum == target:
            break
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return result

n = int(input("Enter number of temperatures: "))

temps = []
for i in range(n):
    num = int(input("Enter temperature: "))
    temps.append(num)

target = int(input("Enter target temperature: "))

result = closest_pair(temps, target)

print("Closest Pair:", result)