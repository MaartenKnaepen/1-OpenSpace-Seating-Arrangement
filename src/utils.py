def import_csv():
    """
    Reads a CSV file containing names and returns a list of names.
    Returns a list containing names read from the CSV file.
    """
    filename = input('Please provide the path of the file with the names: ')
    with open(filename, 'r') as f:
        names = f.read().splitlines()
    return names


def sublists(names, length):
    """
    Divides a list into sublists of a specified length.
    Parameters:
    - names (list): The list to be divided into sublists.
    - length (int): The desired length of each sublist.

    Returns a list of sublists containing names.
    """
    output = [names[i:i + length] for i in range(0, len(names), length)]
    return output


def to_dict(keys, values):
    """
    Converts two lists into a dictionary where the first list represents keys
    and the second list represents values. If the lists have
    unequal lengths, 'Empty' is used to fill the shorter lists.

    Parameters:
    - keys (list): The list containing keys for the dictionary.
    - values (list): The list containing values for the dictionary.

    Returns a dictionary created from the provided keys and values.
    """
    max_len = max(len(lst) for lst in values)
    for lst in values:
        while len(lst) < max_len:
            lst.append('Empty')

    output = dict(zip(keys, values))
    return output
