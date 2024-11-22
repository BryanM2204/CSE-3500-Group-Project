from binarySearch import binarySearch
from ternarySearch import ternarySearch
from linearSearch import linearSearch
import matplotlib.pyplot as plt
import timeit
import random


def generate_sorted_list(size):
    """Generate a sorted list of unique integers."""
    return sorted(random.sample(range(size * 2), size))

def test_search_algorithm(search_func, array, target):
    """Measure the execution time of a search function."""

    # track time to complete
    start_time = timeit.default_timer()
    result = search_func(array, target)
    end_time = timeit.default_timer()

    # mutiply by 1,000 for milliseconds
    elapsed_time = (end_time - start_time) * 1_000

    return elapsed_time, result

def present_results(results, sizes):
    """Visualize the performance of search algorithms."""

    # iterate throughe every algorithm
    for algo, scenario_data in results.items():
        # iterate through all data under the present scenario
        for scenario, times in scenario_data.items():
            if scenario == "present":
                plt.plot(sizes, times, label=f"{algo} ({scenario})")

    # output graph of data
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (ms)")
    plt.title("Performance Comparison of Search Algorithms")
    plt.legend()
    plt.grid(True)
    plt.xscale('log')  # Use a logarithmic scale for input size
    plt.yscale('log')  # Use a logarithmic scale for time (if needed)
    plt.savefig('./Present')

def not_present_results(results, sizes):
    """Visualize the performance of search algorithms."""
    plt.figure()

    # iterate through each search algorithm
    for algo, scenario_data in results.items():
        # iterate through all data under specific scenario "not_present"
        for scenario, times in scenario_data.items():
            if scenario == "not_present":
                plt.plot(sizes, times, label=f"{algo} ({scenario})")

    # output graph 
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (ms)")
    plt.title("Performance Comparison of Search Algorithms")
    plt.legend()
    plt.grid(True)
    plt.xscale('log')  # Use a logarithmic scale for input size
    plt.yscale('log')  # Use a logarithmic scale for time (if needed)
    plt.savefig('./NotPresent')


def main():
    # Test configurations
    sizes = [10, 100, 1000, 10000, 100000]  # Different input sizes
    scenarios = ["present", "not_present"]  # Whether the target is present or not

    results = {algo: {scenario: [] for scenario in scenarios} 
               for algo in ["Ternary Search", "Binary Search", "Linear Search"]}

    for size in sizes:
        array = generate_sorted_list(size)
        print(f"\nTesting with list size: {size}")

        for scenario in scenarios:
            target = random.choice(array) if scenario == "present" else -1
            
            # Test ternary search
            time_taken, _ = test_search_algorithm(ternarySearch, array, target)
            results["Ternary Search"][scenario].append(time_taken)
            
            # Test binary search
            time_taken, _ = test_search_algorithm(binarySearch, array, target)
            results["Binary Search"][scenario].append(time_taken)
            
            # Test linear search
            time_taken, _ = test_search_algorithm(linearSearch, array, target)
            results["Linear Search"][scenario].append(time_taken)

    # Print results
    for algo, scenario_data in results.items():
        print(f"\n{algo} Results:")
        for scenario, times in scenario_data.items():
            print(f"  {scenario.capitalize()}:")
            for size, time in zip(sizes, times):
                print(f"    Size {size}: {time:.6f} ms")

    print(results)
    
    # output graphs
    present_results(results, sizes)
    not_present_results(results, sizes)

if __name__ == "__main__":
    main()
