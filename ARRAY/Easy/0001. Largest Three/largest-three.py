# Using Comparison

import sys

def findLargestThree(nums):

    if len(nums) < 3:
        print("Invalid Input!")
        return

    largest = secondLargest = thirdLargest = -sys.maxsize

    for i in nums:
        if i > largest:
            thirdLargest = secondLargest
            secondLargest = largest
            largest = i
        elif i > secondLargest:
            thirdLargest = secondLargest
            secondLargest = i
        elif i > thirdLargest:
            thirdLargest = i
    return largest, secondLargest, thirdLargest

nums = [10, 4, 3, 50, 23, 90]
result = findLargestThree(nums)
print(result)


# The time complexity of this solution is O(n) and the space complexity is O(1)

# Explanation: This solution uses a loop to iterate through the array and find the largest, second largest, and third largest elements. The loop runs once for each element in the array, so the time complexity is O(n), where n is the size of the input array. The space complexity is O(1) because only a constant amount of additional space is used to store the largest, second largest, and third largest elements.

#----------------------------------------------------------------

# Using built-in sorting

# def findLargestThree(nums):

#     nums.sort()
#     nums.reverse()

#     return nums[0], nums[1], nums[2]

# nums = [10, 4, 3, 50, 23, 90]
# result = findLargestThree(nums)
# print(result)


# The time complexity of this solution is O(n log n) and the space complexity is O(1)

# Explanation: This solution sorts the array in descending order and returns the first three elements. The time complexity of the sort operation is O(n log n) since it uses an efficient sorting algorithm. After sorting, accessing the first three elements is constant time. Therefore, the overall time complexity is dominated by the sorting step. The space complexity is O(1) because no additional space is used apart from the input array.