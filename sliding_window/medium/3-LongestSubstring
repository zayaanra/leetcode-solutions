class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        chars = set()
        l = 0
        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[i])
            length = max(length, i - l + 1)
        return length 