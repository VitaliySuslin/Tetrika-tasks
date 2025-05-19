def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        parameters = func.__code__.co_varnames[: func.__code__.co_argcount]

        for i, arg in enumerate(args):
            if i < len(parameters):
                param_name = parameters[i]
                expected_type = annotations.get(param_name)
                if expected_type is not None and type(arg) is not expected_type:
                    raise TypeError(
                        f"Аргумент '{param_name}' должен быть типа {expected_type.__name__}, "
                        f"получен {type(arg).__name__}"
                    )

        for param_name, value in kwargs.items():
            expected_type = annotations.get(param_name)
            if expected_type is not None and not isinstance(value, expected_type):
                raise TypeError(
                    f"Аргумент '{param_name}' должен быть типа {expected_type.__name__}, "
                    f"получен {type(value).__name__}"
                )
            
        return func(*args, **kwargs)
    
    return wrapper


@strict
def sum_two(
    a: int,
    b: int
) -> int:
    return a + b