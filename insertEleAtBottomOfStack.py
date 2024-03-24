def insertAtBottom(st, x):
    if not st:
        st.append(x)
    else:
        top_element = st.pop()
        insertAtBottom(st, x)
        st.append(top_element)
    return st

# Example usage:
st = [4, 3, 2, 1, 8]
x = 2
print(insertAtBottom(st, x))  # Output: [2, 4, 3, 2, 1, 8]

