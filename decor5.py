import itertools
def pairwise(iterable):
   for i in range(len(iterable) -1):
       yield iterable[i], iterable[i+1]


if __name__ == '__main__':
    for pair in pairwise(range(100)):
        print(pair)