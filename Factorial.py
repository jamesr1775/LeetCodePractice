
factorial_cache = {}


def factorial(num):
    if num in factorial_cache:
        return factorial_cache[num]
    if num == 1:
        fact_num = 1
    else:
        fact_num = num * factorial(num-1)
    factorial_cache[num] = fact_num
    return fact_num


print factorial(100)
