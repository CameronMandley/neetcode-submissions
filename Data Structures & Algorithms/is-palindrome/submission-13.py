class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while not s[left].isalnum() and left < len(s) - 1:
                left += 1
            while not s[right].isalnum() and right > 0:
                right -= 1
            if s[left].lower() == s[right].lower() or (not s[left].isalnum() and not s[right].isalnum()):
                left += 1
                right -= 1
            else:
                return False
        return True

        