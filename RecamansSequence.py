def recamanSequence(self, n):
        # code here
        sequence = [0]
        unique_values = {0}
    
        for i in range(1, n):
            prev_value = sequence[-1]
    
            next_value1 = prev_value - i
            next_value2 = prev_value + i
    
            if next_value1 >= 0 and next_value1 not in unique_values:
                sequence.append(next_value1)
                unique_values.add(next_value1)
            else:
                sequence.append(next_value2)
                unique_values.add(next_value2)
    
        return sequence
