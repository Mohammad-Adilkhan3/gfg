def isPalindrome(self, S):
		# code here
		t=S[::-1]
		if S==t:
		    return "1"
		else:
		    return "0"
s=input()
print(isPalindrome(s))
