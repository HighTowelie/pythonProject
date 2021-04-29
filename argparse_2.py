import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('filename')
    parser.add_argument('-c', type=int, default=10)
    namespace = parser.parse_args()
    filename = namespace.filename
    count_line = namespace.c

    with open(filename, 'r') as f:
        count_line = 0
        for line in f:
            count_line += 1
        print(count_line)
        for _ in range(count_line):
            print(next(f))

            https: // www.notion.so / 3 - 3
            fe79a24f03045b8b27cca65ed6fa05c