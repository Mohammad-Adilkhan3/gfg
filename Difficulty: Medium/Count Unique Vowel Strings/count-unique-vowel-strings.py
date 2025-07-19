class Solution:
    def vowelCount(self, s):
        #code here
        from math import factorial
        vowels=['a','e','i','o','u']
        tmp=set(s)
        res=0
        present_vowel=[]
        for i in tmp:
            if i in vowels:
                present_vowel.append(i)
        n=len(present_vowel)
        if n!=0:
            res=factorial(n)
        for i in present_vowel:
            res*=s.count(i)    
        return res