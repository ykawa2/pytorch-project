class A:
    pass


def func():
    pass


lambda_func = lambda x: x + 1

print("func:", func.__name__, func.__class__, func.__class__.__name__)  # <class 'function'> function
print("A:", A.__name__, A.__class__, A.__class__.__name__)  # <class 'type'> type
print("A():", A().__class__, A().__class__.__name__)  # <class '__main__.A'> A
print(
    "lambda_func:", lambda_func.__name__, lambda_func.__class__, lambda_func.__class__.__name__
)  # <class 'function'> function
