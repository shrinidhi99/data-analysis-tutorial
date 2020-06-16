path = '/home/shrinidhi/Desktop/ML-model-data.txt'

import io
f1 = open("/home/shrinidhi/Desktop/ML-model-data.txt", "r")
f2 = open("final.txt", "w")
l = []
for x in f1:
    l.append(f'"{x.strip()}",')
f1.close()
for x in l:
    f2.write(x)