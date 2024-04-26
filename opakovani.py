cisla = [2,5,9,6,3,7,1,4,8]

for i in range(0, len(cisla)):
    for j in range(i+1, len(cisla)):
        if cisla[i] >= cisla[j]:
            cisla[i], cisla[j] = cisla[j],cisla[i]
 
print( cisla)

for i in range(0, len(cisla)):
    for j in range(i+1, len(cisla)):
        if cisla[i] <= cisla[j]:
            cisla[i], cisla[j] = cisla[j],cisla[i]

print (cisla)