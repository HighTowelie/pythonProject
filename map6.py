# from operator import add
#
# def my_sum(a,b):
#     return a + b
#
# nums1 = [1, 2, 3]
# nums2 = [1, 2, 3]
#
# print(list(map(add, nums1, nums2)))


help('add')

from operator import add

def my_sum(a, b):
    return a + b


if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]

    # print(list(map(, l1, l2)))

shit = [l1[0] + l2[0], l1[1] + l2[1], l1[2] + l2[2]]
print(shit)