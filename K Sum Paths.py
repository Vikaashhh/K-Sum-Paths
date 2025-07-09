'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def sumK(self, root, k):
        prefix_sum = {0: 1}  # 0 sum ka ek path pehle se maana jata hai
        self.count = 0
        
        def dfs(node, curr_sum):
            if not node:
                return
            
            # Current node tak ka prefix sum
            curr_sum += node.data
            
            # Agar (curr_sum - k) pehle aaya hai, to usse banne wale paths count me jod do
            if (curr_sum - k) in prefix_sum:
                self.count += prefix_sum[curr_sum - k]
            
            # Current sum ko map me add karo
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
            
            # Left aur Right subtree ke liye call karo
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)  # ✅ Corrected here
            
            # Backtrack karte waqt prefix sum ka count kam karo
            prefix_sum[curr_sum] -= 1
        
        dfs(root, 0)
        return self.count
