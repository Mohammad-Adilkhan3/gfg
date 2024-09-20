 def countBuildings(self, height):
        # code here
        cnt=1
        mx=height[0]
        for i in height:
            if mx<i:
                cnt+=1
                mx=i
        return cnt
