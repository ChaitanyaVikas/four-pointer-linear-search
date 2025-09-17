import time
import random

def classic_linear_search(arr, key):
    for i, val in enumerate(arr):
        if val == key:
            return i
    return -1

def four_pointer_linear_search(arr, key):
    steps = 0
    i = 0
    j = len(arr) - 1
    mid = (i + j) // 2
    k = mid + 1

    while True:
        steps += 1
        if i > mid and j < k:
            return -1

        if i < len(arr) and arr[i] == key:
            return i
        if j >= 0 and arr[j] == key:
            return j
        if mid < len(arr) and arr[mid] == key:
            return mid
        if k < len(arr) and arr[k] == key:
            return k

        i += 1
        j -= 1
        mid -= 1
        k += 1

def benchmark():
    sizes = [1000, 5000, 10000, 20000]
    positions = ['start', 'middle', 'end', 'absent']

    for size in sizes:
        print(f"\n📦 Array Size: {size}")
        base_array = list(range(size))

        for pos in positions:
            if pos == 'start':
                key = base_array[0]
            elif pos == 'middle':
                key = base_array[size // 2]
            elif pos == 'end':
                key = base_array[-1]
            elif pos == 'absent':
                key = -1  # guaranteed to be absent

            print(f"🔍 Key Position: {pos}")

            for name, func in [("Classic Linear", classic_linear_search), ("Four-Pointer", four_pointer_linear_search)]:
                arr = base_array.copy()
                start = time.time()
                result = func(arr, key)
                end = time.time()
                print(f"{name:<15} ➤ Index: {result:<5} | Time: {(end - start)*1000:.3f} ms")

if __name__ == "__main__":
    benchmark()
