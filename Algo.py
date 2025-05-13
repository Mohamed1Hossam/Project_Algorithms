#_Algorithm_1

import heapq

def max_product_heap(nums):
    largest_three = heapq.nlargest(3, nums)

    smallest_two = heapq.nsmallest(2, nums)

    product1 = largest_three[0] * largest_three[1] * largest_three[2]
    product2 = smallest_two[0] * smallest_two[1] * largest_three[0]

    return max(product1, product2)


def main():
    try:
        input_str = input("Enter integers separated by spaces: ")
        nums = list(map(int, input_str.strip().split()))

        if len(nums) < 3:
            print("Error: At least 3 integers are required.")
            return

        result = max_product_heap(nums)
        print(f"Maximum product of three numbers: {result}")

    except ValueError:
        print("Error: Please enter valid integers.")


if __name__ == "__main__":
    main()


#################################################################################


#_Algorithm_2

def max_product_recursive(nums):
    def recurse(index, max1, max2, max3, min1, min2):
        if index == len(nums):
            product1 = max1 * max2 * max3
            product2 = min1 * min2 * max1
            return max(product1, product2)

        num = nums[index]

        if num >= max1:
            max3, max2, max1 = max2, max1, num
        elif num >= max2:
            max3, max2 = max2, num
        elif num >= max3:
            max3 = num

        if num <= min1:
            min2, min1 = min1, num
        elif num <= min2:
            min2 = num

        return recurse(index + 1, max1, max2, max3, min1, min2)

    return recurse(0, float('-inf'), float('-inf'), float('-inf'), float('inf'), float('inf'))

def main():
    try:
        input_str = input("Enter integers separated by spaces: ")
        nums = list(map(int, input_str.strip().split()))

        if len(nums) < 3:
            print("Error: At least 3 integers are required.")
            return

        result = max_product_recursive(nums)
        print(f"Maximum product of three numbers: {result}")

    except ValueError:
        print("Error: Please enter valid integers.")

if __name__ == "__main__":
    main()

