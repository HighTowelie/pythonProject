
from itertools import repeat

def my_round(num):
    return round(num,2)


my_floats = [
    4.356345,
    6.0934,
    3.245235,
    9.77545,
    2.164234234,
    8.884234235,
    4.595235346645
]
print(list(map(my_round, my_floats)))
print(list(map(round, my_floats, [2] * len(my_floats))))
print(list(map(round, my_floats, repeat(2))))

shit = [round(nums, 2) for nums in my_floats]
print(shit)



