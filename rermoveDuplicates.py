def removeDups(self, str):
		# code here
		s=""
		for i in str:
		    if i not in s:
		        s=s+i
		return s
