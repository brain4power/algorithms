# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Pn < n (ln n + ln ln n − ½) при n > 20, где Pn — n-е простое число.
import math
import cProfile
import timeit


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

# cProfile.run('my_search_prime(1000000)')
# 100 loops, best of 5: 15.6 usec per loop - 10
# 100 loops, best of 5: 334 usec per loop  - 100
# 100 loops, best of 5: 6.17 msec per loop - 1000

#  1    0.000    0.000    0.001    0.001 task_02.py:10(my_search_prime) - 100
#  1    0.002    0.002    0.011    0.011 task_02.py:10(my_search_prime) - 1000
#  1    0.023    0.023    0.152    0.152 task_02.py:10(my_search_prime) - 10000
#  1    0.292    0.292    4.085    4.085 task_02.py:10(my_search_prime) - 100000
#  1    3.450    3.450  122.903  122.903 task_02.py:10(my_search_prime) - 1000000


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

# 100 loops, best of 5: 13.5 usec per loop - 10
# 100 loops, best of 5: 94.2 usec per loop - 100
# 100 loops, best of 5: 1.42 msec per loop - 1000
# 100 loops, best of 5: 19 msec per loop   - 10000


# cProfile.run('search_prime_eratosthenes(10000000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    1    0.000    0.000    0.000    0.000 task_02.py:46(search_prime_eratosthenes) - 100
#    1    0.000    0.000    0.003    0.003 task_02.py:46(search_prime_eratosthenes) - 1000
#    1    0.001    0.001    0.028    0.028 task_02.py:46(search_prime_eratosthenes) - 10000
#    1    0.006    0.006    0.352    0.352 task_02.py:46(search_prime_eratosthenes) - 100000
#    1    0.067    0.067    3.988    3.988 task_02.py:46(search_prime_eratosthenes) - 1000000
#    1    0.622    0.622   50.027   50.027 task_02.py:46(search_prime_eratosthenes) - 10000000

# n = 10000000
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   50.027   50.027 <string>:1(<module>)
#         1    0.622    0.622   50.027   50.027 task_02.py:46(search_prime_eratosthenes)
#         1   48.584   48.584   49.405   49.405 task_02.py:52(primes_sieve)
#         1    0.000    0.000   50.027   50.027 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method math.log}
#  10239202    0.821    0.000    0.821    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


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

#cProfile.run('search_prime_eratosthenes_yield(10000000)')

# n = 10000000
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   50.803   50.803 <string>:1(<module>)
#         1    2.518    2.518   50.803   50.803 task_02.py:90(search_prime_eratosthenes_yield)
#  10000001   48.285    0.000   48.285    0.000 task_02.py:96(primes_sieve)
#         1    0.000    0.000   50.803   50.803 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 100 loops, best of 5: 1.42 msec per loop - 1000
# 100 loops, best of 5: 19.4 msec per loop - 10000
# 100 loops, best of 5: 291 msec per loop  - 100000
# -------------------------------------------------------
# Из текущих алгоритмов самый быстрый оказался через решето Эратосфена.
# Итересно посмотреть разницу в используемой памяти между 2 и 3 алгоритмами. она есть вообще?
# прироста в скорости на исследуемых параметрах не было получено/




