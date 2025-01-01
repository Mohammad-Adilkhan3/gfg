#User function Template for python3


class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        from collections import defaultdict
        anagram_map = defaultdict(list)
        # Iterate through the strings and group by sorted characters
        for string in arr:
            sorted_str = ''.join(sorted(string))
            anagram_map[sorted_str].append(string)
        # Convert grouped values to a list of lists
        return list(anagram_map.values())



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends