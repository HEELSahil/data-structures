# Method 1

def evenGreater(nums):
    for i in range(1, len(nums)):
        if i % 2 == 0:
            if(nums[i] > nums[i - 1]):
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
        else: 
            if(nums[i] < nums[i - 1]):
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
    return nums

nums = [3,5,1,8,9,6,4,7]
result = evenGreater(nums)
print(result)


# The time complexity of this solution is O(n) and the space complexity is O(1)

# Explanation: This solution uses a single loop to iterate through the array and compare adjacent elements. The loop runs once for each element in the array, so the time complexity is O(n), where n is the size of the input array. Within the loop, there is a constant-time comparison and potential swapping of elements. The space complexity is O(1) because only a constant amount of additional space is used. No extra data structures or allocations are required.