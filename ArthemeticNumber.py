def inSequence(self, A, B, C):
        # code here
        if C == 0:
            if A == B:
                return 1
            else:
                return 0
        elif (B-A)%C == 0 and (B-A)//C>=0:
            return 1
        else:
            return 0
