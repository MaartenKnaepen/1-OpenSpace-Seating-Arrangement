def import_csv():
    filename = input('Please provide the path of the file with the names: ')
    with open(filename,'r') as f:
        names = f.read().splitlines()
    return names
   

def sublists(names, length):
    output = [names[i:i+length] for i in range(0,len(names),length)]
    return output

def to_dict(keys, values):
    max_len = max(len(lst) for lst in values)
    for lst in values:
        while len(lst) < max_len:
            lst.append('Empty')

    output = dict(zip(keys, values))
    return output

