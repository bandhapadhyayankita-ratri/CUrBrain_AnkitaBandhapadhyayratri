
scores_input = input("Enter scores separated by commas: ")

scores = []

if scores_input.strip() != "":
    for value in scores_input.split(","):
        scores.append(int(value.strip()))

has_highest = False
has_second = False

highest = 0
second_highest = 0

for score in scores:
    if not has_highest or score > highest:
        if has_highest:
            second_highest = highest
            has_second = True

        highest = score
        has_highest = True

    elif score != highest:
        if not has_second or score > second_highest:
            second_highest = score
            has_second = True

if has_second:
    print(second_highest)
else:
    print(-1)

