contents = ["carrots "
            "sliced",
            "carrot sliced",
            "slicing process"]

filenames = ["docs.txt","report.txt","presentation.txt"]

for content, filename in zip(contents,filenames):
    file = open(f"../files/{filename}",'w')
    file.write(content)

a = (" I am a string of "
     "my own")