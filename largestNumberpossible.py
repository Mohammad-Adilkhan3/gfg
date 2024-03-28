def findLargest(self, N, S):
        # code here
        limit=9*N
        if (S==0 and N>1) or limit<S:
            return -1
            
        elif S==0 and N==1:
            return 0
            
        ans=""
            
        while S!=0:
            if 9<=S:
                ans+="9"
                S-=9
                
            else:
                ans+=str(S)
                S-=S
        if len(ans)==N:
            return int(ans)
            
        else:
            ans+="0"*(N-len(ans))
            return int(ans)

