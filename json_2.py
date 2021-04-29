import json
FILENAME = 'test_1.txt'

def to_json_file(obj, filename, indent=1):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=indent)


if __name__ == '__main__':
    dict_pickle = {
        1: 1,
        "2": 5,
        (5, 7): "test",
        "str": [122, 0x123, 123],
        "tuple": (1, 2, 3),
        "d": {1: 5},
        "func": read_binary
    }
    to_json_file(dict_pickle, 'output.json')
