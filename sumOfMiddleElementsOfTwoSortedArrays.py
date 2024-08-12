def sum_of_middle_elements(self, arr1, arr2):
        # code here
        S=(arr1+arr2)
        S.sort()
        n=len(S)
        return S[n//2]+S[(n//2)-1]
