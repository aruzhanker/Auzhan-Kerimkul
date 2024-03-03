file = open('zara.txt', 'w')
mylist = ['zara is the best store', 'i am Aruzhan', 1, 115]
for i in mylist:
    file.write(str(i) + '\n')
file.close()
f = open('zara.txt', 'r')
print(f.read())