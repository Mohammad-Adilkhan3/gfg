def max_meetings(S, F, N):
    # Create a list of tuples (start, finish, index)
    meetings = [(S[i], F[i], i + 1) for i in range(N)]

    # Sort meetings based on finish times
    meetings.sort(key=lambda x: x[1])

    result = []

    # Select the first meeting
    result.append(meetings[0][2])

    # Initialize the finish time of the last selected meeting
    last_finish = meetings[0][1]

    # Iterate through the rest of the meetings
    for i in range(1, N):
        # If the meeting starts after the finish time of the last selected meeting, select it
        if meetings[i][0] > last_finish:
            result.append(meetings[i][2])
            last_finish = meetings[i][1]

    # Sort the result based on the original meeting indices
    result.sort()

    return result

# Example with given input
N = 10
S = [12, 6, 16, 12, 6, 9, 16, 6, 17, 5]
F = [17, 13, 16, 18, 17, 10, 18, 12, 18, 11]

result = max_meetings(S, F, N)
print("Output:", result)
