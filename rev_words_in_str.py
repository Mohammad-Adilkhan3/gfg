def reverseWords(self,S):
        # code here
        s=S.split(".")
        s.reverse()
        return ".".join(s)
s=input()
print(reverseWords(s))
