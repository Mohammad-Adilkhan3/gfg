#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends


class Solution:
    def evaluate(self, arr):
        # code her
        stack = []
        for token in arr:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()  # Second operand
                a = stack.pop()  # First operand
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))  # Truncate towards zero
            else:  # Operand (number)
                stack.append(int(token))
    
        return stack[0]


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = input().split()
        solution = Solution()
        print(solution.evaluate(arr))
        print("~")

# } Driver Code Ends