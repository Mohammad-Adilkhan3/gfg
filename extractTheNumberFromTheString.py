def ExtractNumber(self,sentence):
        #code here
        n=[int(s) for s in sentence.split() if s.isdigit() and '9' not in s]
        if len(n)!=0:
            return max(n)
        else:
            return -
