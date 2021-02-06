def divisors(integer):
    result = []

    for i in range(2,integer):
        if integer % i == 0:
            result.append(i)
    
    return result if len(result) > 0 else "{} is prime".format(integer)
