# https://leetcode-cn.com/problems/length-of-last-word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not len(s.split()):
            return 0
        return len(s.split()[-1])


test = Solution()

res = test.lengthOfLastWord(" ")
print(res)