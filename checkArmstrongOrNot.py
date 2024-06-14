def armstrongNumber (self, n):
        # code here 
        temp=n
        s=0
        for i in range(3):
            r=n%10
            s=s+r**3
            n=n//10
        if temp==s:
            return "true"
        else:
            return "false"
