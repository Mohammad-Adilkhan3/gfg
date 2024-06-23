def bracket_numbers(s):
    stack = []
    result = []
    counter = 1
    
    for char in s:
        if char == '(':
            stack.append(counter)
            result.append(counter)
            counter += 1
        elif char == ')':
            result.append(stack.pop())
    
    return result
