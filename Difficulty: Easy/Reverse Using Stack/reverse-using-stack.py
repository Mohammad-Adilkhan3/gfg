class Solution:
    def reverse(self, s: str) -> str:
        #code here 
        t=""
        st=[]
        for i in s:
            st.append(i)
        for i in range(len(st)):
            t+=st.pop()
        return t