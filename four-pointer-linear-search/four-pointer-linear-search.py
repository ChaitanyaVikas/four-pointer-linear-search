def four_pointer_linear_search(nums, key):
    steps = 0
    i = 0
    j = len(nums) - 1
    mid = (i + j) // 2
    k = mid + 1

    while True:
        steps += 1

        if i > mid and j < k:
            return f"{key} not found, steps = {steps}"

        if i < len(nums) and nums[i] == key:
            return f"{key} found at index {i}, steps = {steps}"
        if j >= 0 and nums[j] == key:
            return f"{key} found at index {j}, steps = {steps}"
        if mid < len(nums) and nums[mid] == key:
            return f"{key} found at index {mid}, steps = {steps}"
        if k < len(nums) and nums[k] == key:
            return f"{key} found at index {k}, steps = {steps}"

        i += 1
        j -= 1
        mid -= 1
        k += 1

def main():
    nums = list(map(int, input("Enter numbers: ").split()))
    key = int(input("Enter key: "))
    result = four_pointer_linear_search(nums, key)
    print(result)

if __name__ == "__main__":
    main()
