
# Attempt 1
# def fibonacci(position):
#     if position == 1 or position == 2:
#         return 1
#     return fibonacci(position - 2) + fibonacci(position - 1)

# Attempt 2
# def fibonacci(position):
#     if position == 0 or position == 1:
#         return 1
#     return fibonacci(position - 2) + fibonacci(position - 1)

# Attempt 3
# def fibonacci(position):
#     if position <= 0:
#         raise ValueError('position must be non-negative')
#     if position == 0 or position == 1:
#         return 1
#     return fibonacci(position - 2) + fibonacci(position - 1)

# Attempt 4
def fibonacci(position):
    if position < 0:
        raise ValueError('position must be non-negative')
    if position == 0 or position == 1:
        return 1
    return fibonacci(position - 2) + fibonacci(position - 1)
