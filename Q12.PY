
def modulo_power(base, power, MOD):
    result = 1 % MOD

    for i in range(power):
        result = (result * base) % MOD

    return result

base = int(input("Enter the base: "))
power = int(input("Enter the power: "))
MOD = int(input("Enter MOD: "))

print("Result:", modulo_power(base, power, MOD))