# Method 1 using for loop

def arrayEvenAndOdd(nums):

    j = 0

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums


# The time complexity of this solution is O(n) and the space complexity is O(1)

# Explanation: This solution uses a for loop to iterate through the array and moves all even elements to the beginning of the array. The loop runs once for each element in the array, so the time complexity is O(n), where n is the size of the input array. The space complexity is O(1) because only a constant amount of additional space is used.

#----------------------------------------------------------------

# Method 2 using while loop

# def arrayEvenAndOdd(nums):

#     i = 0
#     j = 0
#     n = len(nums)

#     while (i != n):
#         if nums[i] % 2 == 0:
#             nums[i], nums[j] = nums[j], nums[i]
#             j += 1
#         i += 1
#     return nums

# nums = [2,1,3,5,7,9,4,6,8,12]
# result = arrayEvenAndOdd(nums)
# print(result)

# The time complexity of this solution is O(n) and the space complexity is O(1)

# Explanation: This solution uses a while loop to iterate through the array and moves all even elements to the beginning of the array. The loop runs until the index i reaches the length of the array, so the time complexity is O(n), where n is the size of the input array. The space complexity is O(1) because only a constant amount of additional space is used.