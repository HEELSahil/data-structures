# Method 1: Reverse Subarrays Rotation

def rotateArrayRight(nums, d):

    n = len(nums)
    nums[0:n-d] = nums[0:n-d][::-1]
    nums[n-d:n] = nums[n-d:n][::-1]
    nums[0:n] = nums[0:n][::-1]
    return nums
 
nums = [1, 2, 3, 4, 5]
d = 2
print(rotateArrayRight(nums, d))


# The time complexity of this solution is O(n) and the space complexity is O(1)

# Explanation: This solution rotates the array in-place by reversing subarrays. It performs three reverse operations on different portions of the array. Each reverse operation takes linear time, so the overall time complexity is O(n), where n is the size of the input array. The space complexity is O(1) because only a constant amount of additional space is used.

#----------------------------------------------------------------

# Method 2: Reversal Algorithm Rotation

# def reverseArray(nums, start, end):
    
#     while(start < end):
#         nums[end], nums[start] = nums[start], nums[end]
#         start += 1
#         end -= 1

# def rotateArrayRight(nums, d):
#     if d == 0:
#         return nums
#     n = len(nums)
#     reverseArray(nums, 0, n-d-1)
#     reverseArray(nums, n-d, n-1)
#     reverseArray(nums, 0, n-1)
#     return nums

# nums = [1, 2, 3, 4, 5, 6, 7]
# d = 0
# print(rotateArrayRight(nums, d))


# The time complexity of this solution is O(n) and the space complexity is O(1)

# Explanation: This solution rotates the array in-place using the reversal algorithm. It reverses three portions of the array to achieve the rotation. Each reversal operation takes linear time, so the overall time complexity is O(n), where n is the size of the input array. The space complexity is O(1) because only a constant amount of additional space is used.

#----------------------------------------------------------------

# Method 3: Temporary Array Rotation

# def rotateArrayRight(nums, d):
#     n = len(nums)
#     temp  = [0] * n
#     for i in range(n):
#         if i < d:
#             temp[i] = nums[i + (n - d)]
#         else:
#             temp[i] = nums[i - d]
#     return temp


# nums = [1, 2, 3, 4, 5, 6, 7] 
# d = 3
# print(rotateArrayRight(nums, d))


# The time complexity of this solution is O(n) and the space complexity is O(n)

# Explanation: This solution creates a temporary array temp to store the rotated elements. It iterates through the input array nums using a for loop, which runs once for each element in the array. The time complexity is O(n), where n is the size of the input array. The space complexity is O(n) because the solution creates a new array temp of the same size as the input array nums.