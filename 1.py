# plot age and  'overall', age and overall skill

import matplotlib.pyplot as plt 
import csv

x = []
y = []
with open('data.csv', 'r', encoding='utf8') as datafifa:
    data = csv.reader(datafifa)
    for i in data:
        x.append(i[3])
        y.append(i[7])
# print(x)
# print(y)

# Change the data to int
x1 = list(map(int, x[1:18208]))
y1 = list(map(int, y[1:18208]))


# for 1 color graph
# xy = []
# n = 0
# while n < len(x1):
#     xy.append([x1[n],y1[n]])
#     n += 1
# print(xy)

xa = []
ya = []
xb = []
yb = []
xc = []
yc = []
xd = []
yd = []
for a in range(len(x1)):
    # print(x1[a], y1[a] )
    if x1[a] <=25 and y1[a] >= 85:
        xa.append(x1[a])
        ya.append(y1[a])
    elif x1[a] <=25 and y1[a] < 85:
        xb.append(x1[a])
        yb.append(y1[a])
    elif x1[a] > 25 and y1[a] >= 85:
        xc.append(x1[a])
        yc.append(y1[a])
    else:
        xd.append(x1[a])
        yd.append(y1[a])

plt.plot(xa, ya, 'r.', label='A<25 O>85')
plt.plot(xb, yb, 'g.', label='A<25 O<85')
plt.plot(xc, yc, 'b.', label='A>25 O>85')
plt.plot(xd, yd, 'y.', label='A>25 O<85')

plt.xlabel('Age')
plt.ylabel('Overal')
plt.title('Relation between \n Age and Overall')
plt.grid(True)
plt.legend()

plt.show()