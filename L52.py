#Grace Anspach and and Breanna Eafon
def perfect_number(number):
    divisors_sum=0
    for i in range(1, number):
        if number%i==0:
            divisors_sum += i
    if divisors_sum == number:
        return True
    else:
        return False

print(perfect_number(10000))
