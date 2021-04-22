def check_iter_obj(fn):
    def wrapper(*args, **kwargs):
        for index, arg in enumerate(args, start=1):
            try:
                iter(arg)
            except TypeError:
                msg = 'Объект не является итерируемым'
                raise TypeError(msg)
        result = fn(*args,**kwargs)
        return result
    return wrapper

@check_iter_obj
def tmp_1(str_):
    pass


if __name__ == '__main__':
    tmp_1('123')
    tmp_1(12)

def decor_check_kwargs (fn):
    def wrapper(*args, **kwargs):
        for kwarg_name, kwarg-value in kwargs.items():
            try:
                iter(arg)
            except TypeError:
        msg = 'Объект не является итерируемым'
        raise TypeError(msg)
result = fn(*args, **kwargs)
return result
return wrapper