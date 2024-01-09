def search(txt, pat):
    result = []
    n = len(txt)
    m = len(pat)

    for i in range(n - m + 1):
        if txt[i:i+m] == pat:
            result.append(i + 1)

    return result if result else [-1]

# Example usage:
txt1 = "geeksforgeeks"
pat1 = "geek"
output1 = search(txt1, pat1)
print("Output 1:", output1)

txt2 = "abesdu"
pat2 = "edu"
output2 = search(txt2, pat2)
print("Output 2:", output2)
