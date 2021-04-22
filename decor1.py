# def decorator(fn):
#     def wrapper:
#         ...
#         result = fn()
#         ...
#         return result
#     return wrapper()
def make_string_upper(fn):
    def wrapper(string):
        string = string.upper()
        result = fn(string)
        ...
        return result
    return wrapper


@make_string_upper
def print_text(string):
    print(string)


if __name__  == '__main__':

    print_text('faf')
