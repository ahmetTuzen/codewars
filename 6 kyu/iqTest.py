def iq_test(numbers):
    result = [int(number) % 2 for number in numbers.split()]
    for i in range(len(result)):
        if sum(result) == 1 and result[i] % 2 == 1:
            return i + 1
        elif sum(result) > 1 and result[i] % 2 == 0:
            return i + 1
