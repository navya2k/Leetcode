# 15. 3Sum
# Medium
# 29.1K
# 2.6K
# Companies
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = set()
        for i in range(len(nums)):

            l = i+1
            r = len(nums)-1

            while l<r:
                if nums[l] + nums[r] == -nums[i]:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l+=1
                    r-=1
                elif nums[l] + nums[r] < -nums[i]:
                    l+=1
                elif nums[l] + nums[r] > -nums[i]:
                    r-=1
        return list(res)                
                    
        

        