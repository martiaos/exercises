def count_chars(str): #define count
    str = str.lower() #lowercase
    count = {} #empty dict
    for char in str: #for each char in string
        if char in count: #if key in dict
            count[char] += 1 #add 1 to value
        else: #if not
            count[char] = 1 #add dictionary value
    return count #return dictionary

example = "Hello, world!" #string

dictionary = count_chars(example) #function call for example

print('Sorting: Alphabetical \n ')
for char, count in sorted(dictionary.items()):
    print('{:3}{:10}'.format(char, count))

print('\n Sorting: Numerical \n ')
for char, count in sorted(dictionary.items(), key = lambda x: x[1]):
    print('{:3}{:10}'.format(char, count))
