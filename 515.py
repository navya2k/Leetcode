# 515. Find Largest Value in Each Tree Row
# Medium

# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

# Example 1:


# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
# Example 2:

# Input: root = [1,2,3]
# Output: [1,3]
 

# Constraints:

# The number of nodes in the tree will be in the range [0, 104].
# -231 <= Node.val <= 231 - 1



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return 
        st=[(root,0)]
        i=0
        maxi=[root.val]
        while st:
            x,j=st.pop()
            #print(x)
            
            if len(maxi)<=j:
                maxi.append(x.val)
                
            else:
                
                maxi[j]=max(maxi[j],x.val)

            if x.left:st.append((x.left,j+1))
            if x.right:st.append((x.right,j+1))
        #maxi.insert(0,root.val)
        return maxi



        