class Solution():
    def checkRedundancy(self, s):
        # code here 
        st=[]
        op=set("+-*/")
        for i in s:
            if i==")":
                has_op=False
                while st and st[-1]!="(":
                    if st[-1] in op: has_op=True
                    st.pop()
                if not has_op:
                    return True
                st.pop()
            st.append(i)
        return False
            
            