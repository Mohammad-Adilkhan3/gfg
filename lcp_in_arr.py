 def longestCommonPrefix(self, arr, n):
        # code here
        min_str = min(len(a) for a in arr)
        S = ''
        for i in range(min_str):
            key = arr[0][i]
            for item in arr:
                if(item[i] != key):
                    if S == '':
                        return -1
                    return S
            S += key
        return S
n=int(input())
a=list(map(int,input().split()))
res=longestCommonPrefix(a,n)
print(res)
