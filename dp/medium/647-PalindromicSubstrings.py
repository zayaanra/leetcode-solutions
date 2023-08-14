class Solution:
    def count(self, s, l, r):
        c = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            c += 1
            l -= 1
            r += 1
        return c

    def countSubstrings(self, s: str) -> int:
        palindromes = 0
        for i in range(len(s)):
            # odd length
            palindromes += self.count(s, i, i)
            # even length
            palindromes += self.count(s, i, i+1)
        
        return palindromes