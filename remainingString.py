def printString(self, s, ch, count):
		# code here
		cnt=0
		for i in range(len(s)):
		    if s[i]==ch:
		        cnt+=1
	        if cnt==count:
	            return s[i+1:]
	    return ""
