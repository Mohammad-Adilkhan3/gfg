class Solution:
    def substrk(self,s,l,k):
        f=0
        dct={}
        i,j=0,0
        cnt=0
        for i in range(0,l):
            while j<l and len(dct)<k:
                if s[j] not in dct:
                    dct[s[j]]=1
                    
                else:
                    dct[s[j]]+=1
                    
                j+=1
            if len(dct)>=k:
                cnt+=l-j+1
            
            dct[s[i]]-=1
            if dct[s[i]]==0:
                del dct[s[i]]
            
        return cnt
        
    def countSubstr (self, s, k):
        # Code here
        l=len(s)
        return self.substrk(s,l,k)-self.substrk(s,l,k+1)