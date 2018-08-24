with open("p022_names.txt", 'r') as data:
    for line in data:
        names = line.strip('"').split('","')
        names.sort()
