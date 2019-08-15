# attempt to use Memoization to reduce repeat processing
# def memo (func):
#     store = {}
#     def helper (x):
#         if x not in store:
#             store[x] = func(x)
#         return store[x]
#     return helper

def fib_series (max_value):
    stored_values = [1, 1]
    this_value = stored_values[-1] + stored_values[-2]
    while this_value < max_value:
        stored_values.append(this_value)
        this_value = stored_values[-1] + stored_values[-2]
    return stored_values

if __name__ == "__main__":
    # fib_series = memo(fib_series)
    data = fib_series(4000000)
    # fib is odd, odd, even and repeat
    even_sum = sum([data[x] for x in range(2, len(data), 3)])
    print(even_sum)