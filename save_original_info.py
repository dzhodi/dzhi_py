"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func

print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий

До применения вашего декоратор будет вызываться AttributeError при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция

Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""
import functools


def get_info(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.name = func.__name__
        wrapper.doc = func.__doc__
        wrapper.args = args
        wrapper.kwargs = kwargs
        wrapper.__original_func = func
        return result
    return wrapper


def print_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper


@get_info
@print_result
def custom_sum(*args):
    """Returns the sum of all arguments."""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum(1, 2, 3, 4, 5)
    custom_sum(1, 2, 3, 4)

    print(custom_sum.doc)
    print(custom_sum.name)
    without_print = custom_sum.__original_func

    without_print(*custom_sum.args, **custom_sum.kwargs)
