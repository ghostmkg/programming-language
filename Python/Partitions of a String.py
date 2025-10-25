# Global lists to track current partition and final list of partitions
lst = []
temp = []

def all_partitions(s):
    """
    Generate all possible partitions of the given string.

    Each partition is formed by splitting the string into substrings
    in every possible way.

    Parameters:
        s (str): Input string to be partitioned.

    Returns:
        list[list[str]]: A list of partitions, where each partition is a list of substrings.
    """
    
    # Clear previous results if function is reused
    lst.clear()
    temp.clear()
    
    helper(s)  # Call the recursive helper
    return lst


def helper(s):
    """
    Recursive helper function to generate partitions.

    Splits the string into every possible prefix and recurses
    on the remaining suffix.
    """
    
    # If no characters left, store the current partition
    if s == '':
        lst.append(temp[:])  # Add a copy of the current partition
        return

    # Try every possible prefix split
    for i in range(len(s)):
        prefix = s[:i + 1]  # Choose a substring
        temp.append(prefix)  # Add to current construction

        # Recurse on the remaining substring
        helper(s[i + 1:])

        temp.pop()  # Backtrack to explore other partitions


# Example usage:
print(all_partitions("abc"))
# Output:
# [
#   ['a', 'b', 'c'],
#   ['a', 'bc'],
#   ['ab', 'c'],
#   ['abc']
# ]
