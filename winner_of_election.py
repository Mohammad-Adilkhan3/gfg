def winner(arr, n):
    votes_count = {}
    
    # Count the votes for each candidate
    for candidate in arr:
        if candidate in votes_count:
            votes_count[candidate] += 1
        else:
            votes_count[candidate] = 1
    
    max_votes = 0
    winner_name = ""
    
    # Find the candidate with the maximum votes
    for candidate, votes in votes_count.items():
        if votes > max_votes or (votes == max_votes and candidate < winner_name):
            max_votes = votes
            winner_name = candidate
    
    return [winner_name, str(max_votes)]

# Example usage:
n1 = 13
arr1 = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"]
result1 = winner(arr1, n1)
print("Example 1:", result1)

n2 = 3
arr2 = ["andy", "blake", "clark"]
result2 = winner(arr2, n2)
print("Example 2:", result2)
