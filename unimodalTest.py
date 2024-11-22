import math
import time

def unimodal_function(x):
    return -1 * (x - 3)**2 + 7  # Maximum at x = 3

# Ternary Search implementation using the unimodal_function()
def ternary_search(func, left, right, absolute_precision=1e-7):
    while right - left > absolute_precision:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3

        # Compare function values at mid1 and mid2
        if func(mid1) < func(mid2):
            left = mid1
        else:
            right = mid2

    return (left + right) / 2

# Binary search implementation using unimodal_function()
def binary_search_unimodal(func, left, right, absolute_precision=1e-7):
    while right - left > absolute_precision:
        mid = (left + right) / 2

        # Compare function values at mid and mid + small step
        if func(mid) < func(mid + absolute_precision):
            left = mid 
        else:
            right = mid  

    return (left + right) / 2

# Brute Force
def brute_force_search(func, left, right, precision=1e-7):
    step = precision
    max_value = -math.inf
    max_point = None

    x = left
    while x <= right:
        f_value = func(x)
        if f_value > max_value:
            max_value = f_value
            max_point = x
        x += step

    return max_point

# Comparison
def compare_methods():
    # range for search to be conducted
    left, right = 0, 6

    # Ternary Search
    start_time = time.time()
    ternary_result = ternary_search(unimodal_function, left, right)
    ternary_time = time.time() - start_time

    # Binary Search
    start_time = time.time()
    binary_result = binary_search_unimodal(unimodal_function, left, right)
    binary_time = time.time() - start_time

    # Brute Force
    start_time = time.time()
    brute_result = brute_force_search(unimodal_function, left, right)
    brute_time = time.time() - start_time


    print("Ternary Search:")
    print(f"Maximum at x ≈ {ternary_result:.7f}, f(x) ≈ {unimodal_function(ternary_result):.7f}")
    print(f"Execution Time: {ternary_time:.7e} seconds\n")

    print("Binary Search:")
    print(f"Maximum at x ≈ {binary_result:.7f}, f(x) ≈ {unimodal_function(binary_result):.7f}")
    print(f"Execution Time: {binary_time:.7e} seconds\n")

    print("Brute Force:")
    print(f"Maximum at x ≈ {brute_result:.7f}, f(x) ≈ {unimodal_function(brute_result):.7f}")
    print(f"Execution Time: {brute_time:.7e} seconds\n")

compare_methods()
