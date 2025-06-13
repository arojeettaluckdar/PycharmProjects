filenames = ['a.txt', 'b.txt', 'c.txt']
for filename in filenames:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
file.close()


