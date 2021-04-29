FILENAME = 'test.txt'

def read_text_file(filename):
    with open(filename, 'rt', encoding='utf-8') as f:

        for line in f:
            print(line.strip())
            print(line, end='')


if __name__ == '__mailn__':
    read_text_file(FILENAME)



def text_to_bin(filename):
    with open(filename, 'rb') as src_file:
        with open(filename + '_output', 'wb') as dst_file:
            for line in src_file:
                dst_file.write(line)


def read_bin_file(filename):
    with open(filename, 'rb') as f:
        print(f.read())


if __name__ == '__main__':
    # read_bin_file(FILENAME)
    text_to_bin(FILENAME)