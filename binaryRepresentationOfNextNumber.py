def binaryNextNumber(self, s):
		# code here
		x=int(s,2)
		return (bin(x+1)[2:])
