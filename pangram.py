def checkPangram(self,s):
        #code here
        alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
        sentence_set = set(s.lower())
        return alphabet_set.issubset(sentence_set)

