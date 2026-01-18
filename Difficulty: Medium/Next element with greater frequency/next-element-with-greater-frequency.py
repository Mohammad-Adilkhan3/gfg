class Solution:
    def nextFreqGreater(self, arr):
        # code here
        from collections import Counter
        freq=Counter(arr)
        st=[]
        n=len(arr)
        ans=[0]*n
        for i in range(n-1,-1,-1):
            while st and freq[st[-1]]<=freq[arr[i]]:
                st.pop()
            ans[i]=st[-1] if st else -1
            st.append(arr[i])
        return ans
            