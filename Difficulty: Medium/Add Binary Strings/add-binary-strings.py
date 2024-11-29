#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
		# code here
		s1, s2 = s1.lstrip('0')[::-1], s2.lstrip('0')[::-1]
        carry, result = 0, []
        for i in range(max(len(s1), len(s2))):
            total = (int(s1[i]) if i < len(s1) else 0) + (int(s2[i]) if i < len(s2) else 0) + carry
            result.append(str(total % 2))
            carry = total // 2
        if carry: result.append('1')
        return ''.join(result[::-1]) or "0"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends