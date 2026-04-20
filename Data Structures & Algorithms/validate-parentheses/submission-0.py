class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        characters = {')': '(', '}': '{', ']': '['}
        for c in s:
            if stack and stack[-1] == characters.get(c):
                stack.pop()
            else:
                stack.append(c)
        return False if stack else True
    