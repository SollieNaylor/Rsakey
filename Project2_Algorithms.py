import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def test_sorting_algorithm(sort_func, case):
    test_cases = {
        "best": lambda x: x,
        "average": lambda x: sorted(x),
        "worst": lambda x: sorted(x, reverse=True),
    }
    print(f"In {case} case,")
    for N in [100, 1000, 10000]:
        test_data = random.sample(range(N), N)
        start_time = time.time()
        sorted_data = sort_func(test_cases[case](test_data))
        elapsed_time = time.time() - start_time
        print(f"For N = {N}, it takes {elapsed_time:.6f} seconds")

    print(f"In {case} case,")
    while True:
        input_choice = input("Do you want to input another N (Y/N)? ").lower()
        if input_choice == 'n':
            break

        N_value = int(input("What is the N? "))
        test_data = random.sample(range(N_value), N_value)
        start_time = time.time()
        sorted_data = sort_func(test_cases[case](test_data))
        elapsed_time = time.time() - start_time
        print(f"For N = {N_value}, it takes {elapsed_time:.6f} seconds")

# Main program
while True:
    print("Select the sorting algorithm you want to test.")
    print("-------------------------")
    print("1. Bubble Sort")
    print("2. Merge Sort")
    print("3. Quick Sort")
    print("4. Shell Sort")
    print("5. Exit")

    algorithm_choice = int(input("Select a sorting algorithm (1-5): "))

    if algorithm_choice == 5:
        print("Bye!")
        break

    sorting_algorithm = None
    if algorithm_choice == 1:
        sorting_algorithm = bubble_sort
    elif algorithm_choice == 2:
        sorting_algorithm = merge_sort
    elif algorithm_choice == 3:
        sorting_algorithm = quick_sort
    elif algorithm_choice == 4:
        sorting_algorithm = shell_sort
    else:
        print("Please select a valid sorting algorithm.")
        continue

    while True:
        print("Case Scenarios for", "Bubble Sort" if algorithm_choice == 1 else "Merge Sort" if algorithm_choice == 2 else "Quick Sort" if algorithm_choice == 3 else "Shell Sort")
        print("---------------")
        print("1. Best Case")
        print("2. Average Case")
        print("3. Worst Case")
        print("4. Exit", "bubble sort" if algorithm_choice == 1 else "merge sort" if algorithm_choice == 2 else "quick sort" if algorithm_choice == 3 else "shell sort", "test")

        case_choice = int(input("Select the case (1-4): "))

        if case_choice == 4:
            break

        cases = {
            1: "best",
            2: "average",
            3: "worst",
        }

        test_sorting_algorithm(sorting_algorithm, cases[case_choice])
