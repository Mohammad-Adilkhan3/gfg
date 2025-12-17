class Solution:
    def mergeOverlap(self, arr):
        #Code here
        arr.sort(key=lambda x: x[0])
        # Step 2: Merge intervals
        merged = []
        for interval in arr:
            # If the list of merged intervals is empty or there's no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlapping intervals, merge them
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
        


