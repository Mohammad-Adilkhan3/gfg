def anagram(a,b):
  return sorted(a)==sorted(b)
a=input()
b=input()
res=anagram(a,b)
print(res)
