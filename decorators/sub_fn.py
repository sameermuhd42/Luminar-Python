def decorator_sub(fun):
    def wrapper(num1, num2):
        if num1 < num2:
            (num1, num2) = (num2, num1)
        return fun(num1, num2)
    return wrapper


@decorator_sub
def sub(num1, num2):
    return num1 - num2


print(sub(2, 8))


# def decorator_sub(fun):
#     def wrapper(num1, num2):
#         if num1 < num2:
#             return fun(num2, num1)
#     return wrapper
#
#
# @decorator_sub
# def sub(num1, num2):
#     return num1 - num2
#
#
# print(sub(2, 8))

def decorator_div(fun):
    def wrapper(num1, num2):
        if num1 < num2:
            (num1, num2) = (num2, num1)
        return fun(num1, num2)
    return wrapper


def division_by_zero(fun):
    def wrapper(num1, num2):
        if num2 == 0:
            raise Exception('Division by zero')
        else:
            return fun(num1, num2)
    return wrapper


@decorator_sub
@division_by_zero
def div(num1, num2):
    return num1 / num2


try:
    print(div(5, 0))
except Exception as e:
    print(e)

