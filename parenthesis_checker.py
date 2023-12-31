def ispar(self,x):
        # code here
        d={')':'(',']':'[','}':'{'}
       
        stack=[]
        flag=False
        count=0
        if len(x)==1:
            return False
        
       
        for i in x:
            if i in d.values():
                stack.append(i)
                
            elif stack:
                if stack.pop()==d.get(i):
                    flag=True
                else:
                    return False
                    break
                    
            elif i in d:
                count+=1
                
        
           
        else:
            if count or stack:
                return False
            elif not stack:
                return True
            else:
                return flag
s=input()
res=ispar(s)
print(res)
