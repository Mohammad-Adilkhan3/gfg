from collections import Counter

def frequency_sort(arr):
    # Count the frequency of each element in the array
    freq = Counter(arr)
    
    # Sort the array first by frequency (in descending order), then by the value (in ascending order)
    arr.sort(key=lambda x: (-freq[x], x))
    
    return arr
