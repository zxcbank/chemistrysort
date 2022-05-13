import codecs

f = codecs.open("note.txt", 'r', "utf-8")
names = f.readlines()
names.sort()
l = codecs.open("note.json", "w", "utf-8")
for i in range(len(names)):
    l.write(str(names[i]))

