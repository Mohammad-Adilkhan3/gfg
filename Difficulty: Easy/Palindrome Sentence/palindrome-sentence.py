class Solution:
	def isPalinSent(self, s):
		# code here
		rev = ''.join(c.lower() for c in s if c.isalnum())
        return rev == rev[::-1]