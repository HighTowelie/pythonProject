import random

n = 100
random_list = [random.randint(-100, 100) for _ in range(n)]

def check(num):
    return (num < 0) and (num % 3 == 0)

# def random_list(a,b):
#     for i in range(-100,100):
#         return list(i)
print(list(filter(check, random_list)))

for value in filter(check, random_list):
    print(value)
