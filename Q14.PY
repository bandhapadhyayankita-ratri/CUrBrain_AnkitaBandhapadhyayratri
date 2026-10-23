
sales_input = input("Enter sales figures: ")
threshold = int(input("Enter threshold: "))

sales = []

if sales_input.strip() != "":
    for value in sales_input.split(","):
        sales.append(int(value.strip()))

result = []

for sale in sales:
    if sale >= threshold:
        result.append(sale)

print(result)
