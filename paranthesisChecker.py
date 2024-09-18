def ispar(self,x):
        # code here
        stack = []
        matching_brackets = {')': '(', '}': '{', ']': '['}
        for char in x:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack[-1] != matching_brackets[char]:
                    return False
                stack.pop()
        return len(stack) == 0
