FILENAME = 'test.txt'

def create_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        while True:
            ns = input('Number of strings')
            if not ns:
                break
            f.write(ns + '\n')
            f.flush()

if __name__ == '__main__':
    create_file(FILENAME)
