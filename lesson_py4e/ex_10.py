fname = input("Enter yout txt file name :")
# gaurdian
fhand = open(fname)

counts = dict()

for line in fhand :
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

list = list()
for (k,v) in counts.items():
    tmp = (v,k)
    list.append(tmp)

list.sort(reverse = True)
#print(list)
for v,k in list[:5]:
    print((k,v))