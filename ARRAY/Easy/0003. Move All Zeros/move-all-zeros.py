# Partitioning the array

def moveAllZeros(nums):

    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return j

nums = [10, 4, 3, 0, 50, 0, 23, 90]
result = moveAllZeros(nums)
print(result)


# The time complexity of this solution is O(n) and the space complexity is O(1)

# Explanation: This solution uses a loop to iterate through the array and moves all non-zero elements to the beginning of the array. The loop runs once for each element in the array, so the time complexity is O(n), where n is the size of the input array. The space complexity is O(1) because only a constant amount of additional space is used.

#----------------------------------------------------------------

# Rearranging the array

# def moveAllZeros(nums):

#     count = 0
#     n = len(nums)

#     for i in range(n):
#         if nums[i] != 0:
#             nums[count] = nums[i]
#             count+=1

#     while count < n:
#         nums[count] = 0
#         count += 1
#     return nums
         
# nums = [10, 4, 3, 0, 50, 0, 23, 90]
# result = moveAllZeros(nums)
# print(result)


# The time complexity of this solution is O(n) and the space complexity is O(1)

# Explanation: This solution uses two pointers, count and i, to iterate through the array. The count pointer keeps track of the current position to place non-zero elements, and the i pointer iterates through the array. The loop runs once for each element in the array, so the time complexity is O(n), where n is the size of the input array. The space complexity is O(1) because only a constant amount of additional space is used.

#----------------------------------------------------------------

# Using built-in sorting

# def moveAllZeros(nums):

#     nums.sort()
#     nums.reverse()

#     return nums

# nums = [10, 4, 3, 0, 50, 0, 23, 90]
# result = moveAllZeros(nums)
# print(result)


# The time complexity of this solution is O(n log n) and the space complexity is O(1)

# Explanation: This solution sorts the array in descending order using a built-in sorting algorithm. The time complexity of the sorting operation is O(n log n), where n is the size of the input array. After sorting, the array contains all non-zero elements followed by zeros. The space complexity is O(1) because no additional space is used apart from the input array.