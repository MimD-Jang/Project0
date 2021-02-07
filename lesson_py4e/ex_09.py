count = dict()
names = ['charlie', 'sheeran', 'adele', 'lukas','lukas','lukas','sheeran','sheeran']
for name in names:
    count[name] = count.get(name, 0) +1
print(count)

for a,b in count.items():
    print(a,b)