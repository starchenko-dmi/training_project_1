def log(filename=False):
    """Функция декоратор с аргументами для логирования данных в консоль или фаил"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                error = None

                message = f"{func.__name__} Ok"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                return result

            except Exception as e:
                error = e
                result = None
                message = f"{func.__name__} error: {error}. Inputs: {args, kwargs}"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                raise

        return wrapper

    return decorator
