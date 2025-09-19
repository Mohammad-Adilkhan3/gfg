class Solution:
    def minParentheses(self, s):
        # code here
        st = []
        count = 0
        for char in s:
            if char == '(':  
                st.append(char)
            elif char == ')':
                if not st: 
                    count +=1
                elif st: 
                    st.pop()
          
        return len(st)+count


        