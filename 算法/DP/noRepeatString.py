# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        dp = [''] * len(s)
        dp[0] = s[0]
        for i in range(1, len(s)):
            if s[i] not in dp[i-1]:
                dp[i] = dp[i-1] + s[i]
            else:
                dp[i] = dp[i-1].split(s[i])[1] + s[i]

        res = sorted(dp, key=lambda x: len(x))
        # print(res)
        return len(res[-1])

test = Solution()

print(test.lengthOfLongestSubstring("dvdf"))