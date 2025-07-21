print("selection sort")
my_list = list(map(int, input("ENTER YOUR LIST: ").split()))
l = len(my_list)
for j in range(0,l-1):
    p = my_list[j]
    ind = j

    for i in range(j,l-1):
        if p > my_list[i+1]:
            p = my_list[i+1]
            ind = i+1
    x = my_list.pop(int(ind))
    my_list.insert(j,p)
    if x != p:
        my_list.append(x)
    

print(my_list)





