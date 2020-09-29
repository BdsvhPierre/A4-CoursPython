# Faire un algorithme qui prend une liste en paramètre et en crée une copie inversé :
# [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]

# Faire un algorithm qui prend une liste en paramètre, et qui crée une nouvelle liste avec les valeurs unique de la première : [1,1,1,3,2,2,3] -> [1, 3, 2]

l2 = []

l = [1, 1, 1, 3, 2, 2, 3]
count = 0
for value in l:
    if value == 1:
        count = count + 1
        if count == 3:
            l2.append(value)
        
    if value == 3:
        count = count + 1
        if count == 4:
            l2.append(value)
        
    if value == 2:
        count = count + 1
        if count == 6:
            l2.append(value)
        
print(l2)