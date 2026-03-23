# Function to create dictionary
# arr is list of tuple. tuple contain name and marks.


def create_dict(arr):

    dict = {}

    # Your code here
    # Hint: use loop to iterate through arr
    # and assign key value to the dict

    for i in range(len(arr)):
        dict[arr[i][0]] = arr[i][1]

    return dict