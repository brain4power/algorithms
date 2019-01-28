import math
from memory_profiler import profile


def my_search_prime(i):

    def check_prime(number):
        if number == 2:
            return True
        if number % 2 == 0 or number <= 1:
            return False

        sqr = int(math.sqrt(number)) + 1

        for divisor in range(3, sqr, 2):
            if number % divisor == 0:
                return False
        return True

    check_number = 2
    search_number = 2
    while i:
        if check_prime(check_number):
            i -= 1
            search_number = check_number
        check_number += 1
    return search_number

@profile(precision=6)
def search_prime_eratosthenes(i):
    if i < 21:
        limit_of_sieve = 73
    else:
        limit_of_sieve = int(i * (math.log(i, math.e) + math.log(math.log(i, math.e), math.e) - 0.5))

    def primes_sieve(limit):
        a = [True] * limit
        a[0] = a[1] = False
        result = []
        for (i, isprime) in enumerate(a):
            if isprime:
                result.append(i)
                for n in range(i*i, limit, i):
                    a[n] = False
        return result

    return primes_sieve(limit_of_sieve)[i - 1]



def search_prime_eratosthenes_yield(i):

    if i < 21:
        limit_of_sieve = 73
    else:
        limit_of_sieve = int(i * (math.log(i, math.e) + math.log(math.log(i, math.e), math.e) - 0.5))

    def primes_sieve(limit):
        a = [True] * limit
        a[0] = a[1] = False
        for (i, isprime) in enumerate(a):
            if isprime:
                yield i
                for n in range(i*i, limit, i):
                    a[n] = False
    for idx, element in enumerate(primes_sieve(limit_of_sieve)):
        if idx == i - 1:
            return element


if __name__ == '__main__':
    search_prime_eratosthenes(10000)


# сделать профайлер памяти самому у меня не получилось(
# Настроил чужой
# но он больше сам памяти кушает, чем рассказывает что почем.

# search_prime_eratosthenes_yield(10000)
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     50  10.449219 MiB  10.449219 MiB   @profile(precision=6)
#     51                             def search_prime_eratosthenes_yield(i):
#     52
#     53  10.449219 MiB   0.000000 MiB       if i < 21:
#     54                                     limit_of_sieve = 73
#     55                                 else:
#     56  10.457031 MiB   0.007812 MiB           limit_of_sieve = int(i * (math.log(i, math.e) + math.log(math.log(i, math.e), math.e) - 0.5))
#     57
#     58  10.457031 MiB   0.000000 MiB       def primes_sieve(limit):
#     59  11.292969 MiB   0.835938 MiB           a = [True] * limit
#     60  11.292969 MiB   0.000000 MiB           a[0] = a[1] = False
#     61  11.292969 MiB   0.000000 MiB           for (i, isprime) in enumerate(a):
#     62  11.292969 MiB   0.000000 MiB               if isprime:
#     63  11.292969 MiB   0.000000 MiB                   yield i
#     64  11.292969 MiB   0.000000 MiB                   for n in range(i*i, limit, i):
#     65  11.292969 MiB   0.000000 MiB                       a[n] = False
#     66  11.292969 MiB   0.000000 MiB       for idx, element in enumerate(primes_sieve(limit_of_sieve)):
#     67  11.292969 MiB   0.000000 MiB           if idx == i - 1:
#     68  11.292969 MiB   0.000000 MiB               return element


# search_prime_eratosthenes(10000)
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     29  10.507812 MiB  10.507812 MiB   @profile(precision=6)
#     30                             def search_prime_eratosthenes(i):
#     31  10.507812 MiB   0.000000 MiB       if i < 21:
#     32                                     limit_of_sieve = 73
#     33                                 else:
#     34  10.515625 MiB   0.007812 MiB           limit_of_sieve = int(i * (math.log(i, math.e) + math.log(math.log(i, math.e), math.e) - 0.5))
#     35
#     36  10.515625 MiB   0.000000 MiB       def primes_sieve(limit):
#     37  11.351562 MiB   0.835938 MiB           a = [True] * limit
#     38  11.351562 MiB   0.000000 MiB           a[0] = a[1] = False
#     39  11.351562 MiB   0.000000 MiB           result = []
#     40  11.726562 MiB   0.003906 MiB           for (i, isprime) in enumerate(a):
#     41  11.726562 MiB   0.000000 MiB               if isprime:
#     42  11.726562 MiB   0.003906 MiB                   result.append(i)
#     43  11.726562 MiB   0.000000 MiB                   for n in range(i*i, limit, i):
#     44  11.351562 MiB   0.000000 MiB                       a[n] = False
#     45  11.726562 MiB   0.000000 MiB           return result
#     46
#     47  11.726562 MiB   0.000000 MiB       return primes_sieve(limit_of_sieve)[i - 1]