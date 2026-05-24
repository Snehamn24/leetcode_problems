Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

# Solution
  class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while(left<right):
            while(left<right and not s[left].isalnum()):
                left+=1
            while(left<right and not s[right].isalnum()):
                right-=1
            if(s[left].lower()!=s[right].lower()):
                return False
            left+=1
            right-=1
        return True

# Time Complexity o(n)
# Space Compelcity o(1)

#other solution
s = "".join(char.lower() for char in s if char.isalnum())
return s[::-1]==s

#but this approcah creates a new string which increases the space complexity to o(n)
