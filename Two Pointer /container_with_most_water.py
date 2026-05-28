# Container with the most water (problem 11)
Example : 1
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example : 2

Input: height = [1,1]
Output: 1

Solution (using two pointer approach , Time Complexity = O(n) and space complexity O(1))
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        total_area = 0
        while(left<right):
            width = right - left
            current_height = min(height[left],height[right])
            current_area = current_height * width
            total_area = max(total_area,current_area)

            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return total_area

# Other approches - using brute force
max_area = 0

for i in range(len(height)):
    for j in range(i + 1, len(height)):
        width = j - i
        h = min(height[i], height[j])
        area = width * h
        max_area = max(max_area, area)

return max_area

# but this approach increases the time complexity to O(n^2) too slow for the larger input 

