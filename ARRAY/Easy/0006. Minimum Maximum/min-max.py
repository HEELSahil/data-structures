# Two Pointer Solution

def minmax(nums):

    n = len(nums)
    l = 0
    r = n - 1
    hash = [None] * n
    
    for i in range(n):
        if i % 2 == 0:
            hash[i] = nums[r]
            r -= 1
        else:
            hash[i] = nums[l]
            l += 1
    return hash

    # Copy hash[] to nums[]
    # for i in range(len(nums)):
    #     nums[i] = hash[i]
    # return nums

nums = [1,2,3,4,5]
result = minmax(nums)
print(result)


# The time complexity of this solution is O(n) and the space complexity is also O(n)

# Explanation: This solution uses a two-pointer approach to fill a new array called hash. It iterates through the input array nums using the loop, which runs once for each element in the array. Within each iteration, the solution determines whether to assign the value from the right pointer (r) or the left pointer (l) to the corresponding position in hash. Both the left and right pointers move independently based on whether the current index is even or odd. The time complexity is O(n) because the loop iterates through each element once. The space complexity is O(n) because the solution creates a new array hash of the same size as the input array nums. Therefore, the space required is proportional to the size of the input array.



