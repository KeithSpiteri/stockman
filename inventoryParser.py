from entry import Entry

def parseInventoryFile(fileName):
    'Assumes that inventory file starts with header line and discards lines beginning with #'
    converted_entries = []
    with open(fileName, 'r') as infile:
        infile.readline()
        for line in infile:
            if (line.startswith('#')):
                continue
            elif (Entry.isValid(line)):
                converted_entries.append(Entry(line))
    return converted_entries