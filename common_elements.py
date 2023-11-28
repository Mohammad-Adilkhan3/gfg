def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        a=set(A)
        b=set(B)
        c=set(C)
        d=a.intersection(b)
        e=d.intersection(c)
        return sorted(list(e))
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
print(commonElements (A, B, C, n1, n2, n3))
