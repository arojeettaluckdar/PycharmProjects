filenames = ["1.Raw Data.txt", "2.Report.txt", "3.Pressentation.txt"]

for filename in filenames:
    filename = filename.replace('.','-',1)
    print(filename)
