# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        length = 0
        old_dp = s[0]
        for i in range(1, len(s)):
            if s[i] not in old_dp:
                dp = old_dp + s[i]
            else:
                dp = old_dp.split(s[i])[1] + s[i]
            length = max(length, len(dp), len(old_dp))
            old_dp = dp
        return length

test = Solution()

print(test.lengthOfLongestSubstring(" aaa"))