print("bubble sort")
my_list = list(map(int, input("ENTER YOUR LIST: ").split()))
l = len(my_list)
for j in range(l):
    for i in range(0,l-1):
        if my_list[i]> my_list[i+1]:
            c = my_list[i]
            my_list[i] = my_list[i+1]
            my_list[i+1]= c

print(my_list)
