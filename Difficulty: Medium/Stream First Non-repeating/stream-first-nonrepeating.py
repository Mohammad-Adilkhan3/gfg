class Solution:
	def firstNonRepeating(self, s):
		# code here
		char=[0]*26
        res=''
        fn=''
        for i in s:
            c=ord(i)-ord('a')
            if char[c]==0:
                a= i if not fn else fn[0]
                fn+=i
            else:
                fn= fn.replace(i, '')
                a=fn[0] if fn else '#'
            res+=a
            char[c]+=1
        return res
        		