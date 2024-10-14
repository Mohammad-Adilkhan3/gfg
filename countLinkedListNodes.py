def getCount(self, head):
        # code here
        cnt=0
        while head:
            cnt+=1
            head=head.next
        return cnt
