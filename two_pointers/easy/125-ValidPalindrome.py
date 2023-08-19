class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted = s.replace(" ", "").lower()
        converted = ''.join(filter(str.isalnum, converted))

        l, r = 0, len(converted)-1

        while l < r:
            if converted[l] != converted[r]:
                return False
            l += 1
            r -= 1
        
        return True