class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # collections deque
        brackets = {'}': '{',
                    ')': '(',
                    ']': '['
                    }

        if not s:
            return False

        for b in s:
            if b in brackets.values():
                stack.append(b)
            else:
                if stack and stack[-1] == brackets[b]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False
