L = []
uvjet = 0
for i in range(165):
    a = input()
    a = a.upper()
    L.append(a)
    if len(a) != 3:
        uvjet = 1

for i in range(165):
    if i > 0:
        print("            ", end = "")
    print("if (random_index = ", end = "")
    print(i, end = "")
    print(") { let rijec = \"", end = "")
    print(L[i], end = "")
    print("\"; }")
    
if uvjet == 1:
    print("NO")
