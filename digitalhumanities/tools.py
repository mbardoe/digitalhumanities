def find_substring(substring, string):
    """ 
    Returns list of indices where substring begins in string

    >>> find_substring('me', "The cat says meow, meow")
    [13, 19]
    """
    indices = []
    index = -1  # Begin at -1 so index + 1 is 0
    while True:
        # Find next index of substring, by starting search from index + 1
        index = string.find(substring, index + 1)
        if index == -1:  
            break  # All occurrences have been found
        indices.append(index)
    return indices

