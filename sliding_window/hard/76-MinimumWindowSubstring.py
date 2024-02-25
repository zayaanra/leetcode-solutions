class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        
        res, resLen = [-1, -1], float("inf")

        cntT = {}
        for c in t:
            cntT[c] = 1 + cntT.get(c, 0)

        window = {}
        have, need = 0, len(cntT)
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in cntT and window[s[r]] == cntT[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in cntT and window[s[l]] < cntT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""