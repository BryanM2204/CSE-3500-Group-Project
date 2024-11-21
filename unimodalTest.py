import matplotlib.pyplot as plt
import time
import numpy as np
import math
import random

# Define the unimodal function (a simple parabola)
def unimodal_function(x):
    """A complex unimodal function with noise to test the algorithms."""
    # Function: sin(x) + (x-5000)^2 / 10000
    # This creates a curve with a global minimum around x = 5000, with a lot of fluctuations
    noise = random.uniform(-0.01, 0.01)  # Adding small random noise
    return math.sin(x) + ((x - 5000)**2) / 10000 + noise

# Ternary Search to find the minimum of a unimodal function
def ternary_search_minimize(f, left, right, epsilon=1e-5):
    while right - left > epsilon:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        if f(mid1) < f(mid2):
            right = mid2
        else:
            left = mid1
    return (left + right) / 2

# Binary Search to find the minimum of a unimodal function
def binary_search_minimize(f, left, right, epsilon=1e-5):
    while right - left > epsilon:
        mid = (left + right) / 2
        if f(mid - epsilon) < f(mid + epsilon):
            right = mid
        else:
            left = mid
    return (left + right) / 2

# Compare performance for a range of sizes
def compare_search_algorithms():
    epsilon = 1e-7  # Precision level
    sizes = np.arange(10, 10000000, 10)  # Search ranges from 10 to 1000
    ternary_times = []
    binary_times = []

    for size in sizes:
        left, right = 0, size  # Define the search range

        # Measure ternary search time
        start_time = time.time()
        ternary_search_minimize(unimodal_function, left, right, epsilon)
        ternary_times.append((time.time() - start_time) * 1_000_000)  # Convert to microseconds

        # Measure binary search time
        start_time = time.time()
        binary_search_minimize(unimodal_function, left, right, epsilon)
        binary_times.append((time.time() - start_time) * 1_000_000)  # Convert to microseconds

    return sizes, ternary_times, binary_times

# Run the comparison and generate a graph
sizes, ternary_times, binary_times = compare_search_algorithms()

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, ternary_times, label='Ternary Search', color='b', marker='o')
plt.plot(sizes, binary_times, label='Binary Search', color='r', marker='x')
plt.xlabel('Search Range Size', fontsize=14)
plt.ylabel('Time (Microseconds)', fontsize=14)
plt.title('Comparison of Ternary Search and Binary Search for Function Minimization', fontsize=16)
plt.legend()
plt.grid(True)
plt.savefig('./unimodal')