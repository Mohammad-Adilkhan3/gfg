def min_sprinklers(self, gallery, n):
        # code here
        sprinklers = []

        for i in range(n):
            if gallery[i] != -1:
                sprinklers.append((i - gallery[i], i + gallery[i]))
    
        sprinklers.sort()
    
        target = 0
        result = 0
        i = 0
    
        while (i < len(sprinklers)) and (target < n):
            start, end = sprinklers[i]
    
            while (i < len(sprinklers)) and (sprinklers[i][0] <= target):
                end = max(end, sprinklers[i][1])
                i += 1
    
            if target < start:
                return -1
    
            target = end + 1
            result += 1
    
        return result if target >= n else -1
