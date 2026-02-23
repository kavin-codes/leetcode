height= [1,8,6,2,5,4,8,3,7]

class Solution:
    def single(self, nums):
        
    
        left = 0
        right = len(height) - 1
        max_area = 0  

        while left < right:
            Height = min(height[left], height[right])
            width = right - left
            area = Height * width
            max_area = max(max_area, area)

            # Move the shorter pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
        


s1 = Solution()
print(s1.single(height)) 