def isPalindrome(self, head):
        #code here
        res=[]
        while head!=None:
            res.append(head.data)
            head=head.next
        return res==res[::-1]
