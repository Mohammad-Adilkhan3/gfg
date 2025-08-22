class Solution:
    #Function to reverse the queue.
    def reverseQueue(self, q):
        # code here
        return rev(q)
def rev(q):
    if q.empty():
        return q
    ele=q.get()
    r=rev(q)
    r.put(ele)
    return r
        