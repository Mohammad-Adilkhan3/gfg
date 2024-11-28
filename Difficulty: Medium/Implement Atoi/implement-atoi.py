#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Step 1: Remove leading whitespaces
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        if i == len(s):
            return 0  # Return 0 if only whitespaces are present
        
        # Step 2: Check for optional sign
        sign = 1  # Default is positive
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # Step 3: Convert valid digits to integer
        num = 0
        while i < len(s) and '0' <= s[i] <= '9':
            digit = int(s[i])  # Get integer value of current character
            # Check for overflow before adding the digit
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + digit
            i += 1
        
        # Step 4: Apply sign and return
        return sign * num



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends