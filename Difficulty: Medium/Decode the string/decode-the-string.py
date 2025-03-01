
class Solution:
    def decodedString(self, s):
        # code here
        nums=[]
        st=[]
        curr=""
        k=0
        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)  
            elif char == '[':
                nums.append(k)  
                st.append(curr)  
                curr = "" 
                k = 0  
            elif char == ']':
                repeat_count = nums.pop() 
                prev_string = st.pop()  
                curr = prev_string + (curr * repeat_count)  
            else:
                curr += char  
    
        return curr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends