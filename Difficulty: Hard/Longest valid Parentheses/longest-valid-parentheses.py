
class Solution:
    def maxLength(self, s):
        # code here
        st=[-1]
        res=0
        for i,p in enumerate(s):
            if p=='(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    res=max(res,i-st[-1])
        return res


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
        print("~")

# } Driver Code Ends