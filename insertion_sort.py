print("insertion sort")
my_list = list(map(int, input("ENTER YOUR LIST: ").split()))
l = len(my_list)
list2 = []
list2.append(my_list[0])
for i in range(1,l):
    p = my_list[i]
    j = 0
    while j < len(list2) and p > list2[j]:
        j=j+1
    if j == len(list2):
        list2.append(p)
    else:
        list2.insert(j,p)
print(my_list,len(my_list))
print(list2,len(list2))
  
