with open("file.txt") as f:
    print(f.read())
print(f.closed)

txt = "useless life"
with open("file.txt", 'w') as f:
    f.write(txt)
print(f.closed)

txt = " useless life wasste."
with open("file.txt", 'a') as f:
    f.write(txt)
print(f.closed)