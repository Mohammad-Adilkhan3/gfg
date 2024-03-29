def evenlyDivides (self, N):
        # code here
        count = 0
        n = [int(i) for i in str(N) if str(i) != '0']
        count = 0
        for i in n:
            if N % i == 0:
                count += 1
        return count
