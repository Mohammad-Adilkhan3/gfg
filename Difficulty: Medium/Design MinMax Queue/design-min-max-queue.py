import heapq
class SpecialQueue:
    def __init__(self):
        # Define Data Structures
        self.queue=[]
        self.min_heap=[]
        self.max_heap=[]
        self.count={}
        

    
    def enqueue(self, x):
        # Insert element into the queue
        self.queue.append(x)
        heapq.heappush(self.min_heap,x)
        heapq.heappush(self.max_heap,-x)
        self.count[x]=self.count.get(x,0)+1

    
    def dequeue(self):
        # Remove element from the queue
        if not self.queue:
            return None
        x=self.queue.pop(0)
        self.count[x]-=1
        return x

    
    def getFront(self):
        # Get front element
        if not self.queue:
            return None
        return self.queue[0]

    
    def getMin(self):
        # Get minimum element
        while self.min_heap and self.count[self.min_heap[0]]==0:
            heapq.heappop(self.min_heap)
        return self.min_heap[0] if self.min_heap else None
        

    
    def getMax(self):
        # Get maximum element
        while self.max_heap and self.count[- self.max_heap[0]]==0:
            heapq.heappop(self.max_heap)
        return - self.max_heap[0] if self.max_heap else None
