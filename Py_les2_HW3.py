# winter = [1, 2, 12]
# spring = [3, 4, 5]
# summer = [6, 7, 8]
# autumn = [9, 10, 11]
# while(1):
#     num_month = int(input("Введите номер месяца в виде целого числа от 1 до 12 :"))
#     if num_month in winter :
#         print("Зима")
#         break
#     elif num_month in spring:
#         print("Весна")
#         break
#     elif num_month in summer:
#         print("Лето")
#         break
#     elif num_month in autumn:
#         print("Осень")
#         break
#     else :
#         print("Ввели неверное число (Только целые числа от 1 до 12), попробуйте еще")
num_month = int(input("Введите номер месяца в виде целого числа от 1 до 12 :"))
season_dict = {1:"Зима", 2:"Зима", 12:"Зима"}
season_dict.update({3:"Весна", 4:"Весна", 5:"Весна"})
season_dict.update({6:"Лето", 7:"Лето", 8:"Лето"})
season_dict.update({9:"Осень", 10:"Осень", 11:"Осень"})
for month_season, season in season_dict.items():
    if num_month == month_season:
        print(season)
        break





