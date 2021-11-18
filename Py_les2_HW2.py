my_list = input("Укажите набор цифр через пробел: ")
my_list = my_list.split()
for index in range(0, len(my_list)-1, 2) :
    my_list[index], my_list[index+1] = my_list[index+1], my_list[index]
print(my_list)
