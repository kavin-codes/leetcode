class Solution:
    def subarraySum(self, nums, k):
        count = 0                
        current_sum = 0           
        prefix_map = {0: 1}   

        for num in nums:
            current_sum += num              
            if (current_sum - k) in prefix_map:
                count += prefix_map[current_sum - k]   
            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1     

        return count


nums = [1, 2, 3]
k = 3

sol = Solution()
print(sol.subarraySum(nums, k)) 
