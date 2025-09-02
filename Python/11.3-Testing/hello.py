print("Hello world!")
print("Hi")

for i in range(1000):
    print(str(i))

li = []
for i in range(10):
    li.append([0] * 10)

li[0][1] = -1
li[3][8] = -1
x = 1
y = 6

li[x][y] = -1

li[x-1][y-1] += 1
li[x][y-1] += 1
li[x+1][y-1] += 1
li[x-1][y] += 1
li[x+1][y] += 1
li[x-1][y+1] += 1
li[x][y+1] += 1
li[x+1][y+1] += 1

for i in li:
    print(i)
