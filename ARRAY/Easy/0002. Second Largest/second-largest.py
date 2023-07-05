# Using Comparison

import sys

def findSecondLargest(nums):

    if(len(nums) < 2):
        print("Invalid Input")
        return

    largest = secondLargest = -sys.maxsize

    for i in nums:
        if i > largest:
            secondLargest = largest
            largest = i
        elif i > secondLargest:
            secondLargest = i
    return secondLargest

nums = [10]
result = findSecondLargest(nums)
print(result)


# The time complexity of this solution is O(n) and the space complexity is O(1)

# Explanation: This solution iterates through the array once to find the largest and second largest elements. The loop runs once for each element in the array, so the time complexity is O(n), where n is the size of the input array. The space complexity is O(1) because only a constant amount of additional space is used to store the largest and second largest elements.

#----------------------------------------------------------------

# Using built-in sorting

def findSecondLargest(nums):

    nums.sort()
    nums.reverse()

    return nums[1]

nums = [10, 4, 3, 50, 23, 90]
result = findSecondLargest(nums)
print(result)


# The time complexity of this solution is O(n log n) and the space complexity is O(1)

# Explanation: This solution sorts the array in descending order and returns the second element. The time complexity of the sort operation is O(n log n) since it uses an efficient sorting algorithm. After sorting, accessing the second element is constant time. Therefore, the overall time complexity is dominated by the sorting step. The space complexity is O(1) because no additional space is used apart from the input array.