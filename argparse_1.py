import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)

    namespace = parser.parse_args()
    print(namespace.a)
    print(namespace.b)
    print(namespace.a + namespace.b)