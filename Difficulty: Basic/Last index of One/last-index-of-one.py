#User function Template for python3

class Solution:
    def lastIndex(self, s: str) -> int:
        # code here
        i=-1
        while i>=-len(s):
            if s[i]=="1":
                return i+len(s)
            i-=1
        return "-1"
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        s = input()
        ob = Solution()
        print(ob.lastIndex(s))

        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends