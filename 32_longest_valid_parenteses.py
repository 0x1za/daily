class Solution:
    OPENING = '('
    def longestValidParentheses(self, s: str) -> int:
        found = 0
        stack = []
        if len(s) != 0:
            for item in s:
                if item == self.OPENING:
                    stack.append(item)
                else:
                    if len(stack) != 0:
                        stack.pop()
                        found += 2
            return found
        else:
            return 0

a = Solution()
print(a.longestValidParentheses("(((())))"))


