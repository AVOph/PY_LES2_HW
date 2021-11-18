my_list = [7, 5, 3, 3, 2]
new_num = int(input("Введите новый элемент рейтинга:"))
if new_num <= my_list[-1]:
    my_list.append(new_num)
    print(f"Пользователь ввел число {new_num}. Результат: {my_list}")
else:
    a = 0
    while a < len(my_list):
        if new_num > my_list[a]:
            my_list.insert(a, new_num)
            print(f"Пользователь ввел число {new_num}. Результат: {my_list}")
            break
        a +=1
