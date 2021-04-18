import random

#
# n = 100
# random_list = [random.randint(-100, 100) for _ in range(n)]
#
# if __name__ == '__main__':
#     count
# print(filter(random_list))

from itertools import count

def pow_2(num):
    return num ** 2
def even_num(num):
    return num % 2 == 0

if __name__ == '__main__':
    iter_even = filter(even_num, count(1))
    iter_pow_2 = map(pow_2, iter_even)


for _ in range(10):
    print(next(iter_pow_2))

print("-" * 20)

for num in iter_pow_2:
    print(num)
    if num > 1000000:
        break