#55. Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            # if nums[0]>0:return True
            # else:return False
            return True
        # maxi=nums[0]
        cur=nums[0]
        n=len(nums)
        for i in range(n):
            cur=max(cur-1,nums[i])
            print(cur)
            if cur==0 and i<n-1:return False
            # maxi=max(maxi,cur)
        return True 

        