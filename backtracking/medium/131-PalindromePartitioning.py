class Solution:
    def isPalindrome(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> list[list[str]]:
        substring = ""
        res = []
        palindromes = []

        def backtrack(i):
            if i >= len(s):
                res.append(palindromes.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(i, j, s):
                    palindromes.append(s[i:j+1])
                    backtrack(j+1)
                    palindromes.pop()

            
        backtrack(0)
        return res