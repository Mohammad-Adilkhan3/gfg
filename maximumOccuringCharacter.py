def getMaxOccurringChar(self,s):
        #code here
        l=[0]*26
        for i in s:
            l[ord(i)-97]+=1
        maxi=max(l)
        for i in range(26):
            if l[i]==maxi:
                return chr(i+97)
