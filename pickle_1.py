import pickle

def to_pickle_file(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)

# dict_pickle = {
#     1: 1,
#     "2": 5,
#     (5, 7): "test",
#     "str": [122, 0x123, 123],
#     "tuple": (1, 2, 3),
#     "d": {1: 5},
#     "func": read_binary
# }
def read_binary():...


if __name__ == '__main__':
    dict_pickle = {...}
    to_pickle_file(dict_pickle, 'tmp.pickle')