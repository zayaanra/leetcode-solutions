class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapping = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        ans = []
        combo = []

        if len(digits) == 0:
            return []


        def backtrack(i, cur):
            if len(cur) == len(digits):
                ans.append(cur)
                return
            
            for ch in mapping[digits[i]]:
                backtrack(i+1, cur + ch)
            
        backtrack(0, "")
        return ans