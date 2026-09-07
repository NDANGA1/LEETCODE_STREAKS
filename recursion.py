def sum(numbers):
    print(f"called sum({numbers})")
    if len(numbers) == 1:
        return numbers[0]
    print(f"doing {numbers[0]} + sum({numbers})")
    return numbers[0] + sum(numbers[1:])


print(sum([1,2,7,5]))