def compareNM(self, n : int, m : int) -> str:
        # code here
        if n<m:
            return "lesser"
        elif m<n:
            return "greater"
        else:
            return "equal"
