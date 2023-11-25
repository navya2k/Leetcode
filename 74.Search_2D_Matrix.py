# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 
class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        l =0 
        r = len(nums)-1
        while l<=r:
            mid=(l+r)//2
            print(mid)
            if nums[mid][0]<=target and nums[mid][len(nums[0])-1]>=target:
                l1=0
                r1=len(nums[0])-1
                while l1<=r1:
                    mid1=(l1+r1)//2
                    if nums[mid][mid1]==target:return True
                    if nums[mid][mid1]<target:l1=mid1+1
                    else:r1=mid1-1
                break

            elif nums[mid][len(nums[0])-1]<target :l=mid+1
            elif nums[mid][0]>target:r=mid-1
        return False

            
            
                


        