import random


#list of meals (name of meal, price to make, ingrediant 1, ingrediant 2, etc.)
Meal_1 = ['name 1', 1, '1ingrediant 1', '1ingrediant 2', '1ingrediant 3', '1ingrediant 4', '1ingrediant 5']
Meal_2 = ['name 2', 2, '2ingrediant 1', '2ingrediant 2', '2ingrediant 3', '2ingrediant 4', '2ingrediant 5']
Meal_3 = ['name 3', 3, '3ingrediant 1', '3ingrediant 2', '3ingrediant 3', '3ingrediant 4', '3ingrediant 5']
Meal_4 = ['name 4', 4, '4ingrediant 1', '4ingrediant 2', '4ingrediant 3', '4ingrediant 4', '4ingrediant 5']
Meal_5 = ['name 5', 5, '5ingrediant 1', '5ingrediant 2', '5ingrediant 3', '5ingrediant 4', '5ingrediant 5']
Meal_6 = ['name 6', 6, '6ingrediant 1', '6ingrediant 2', '6ingrediant 3', '6ingrediant 4', '6ingrediant 5']
Meal_7 = ['name 7', 7, '7ingrediant 1', '7ingrediant 2', '7ingrediant 3', '7ingrediant 4', '7ingrediant 5']
Meal_8 = ['name 8', 8, '8ingrediant 1', '8ingrediant 2', '8ingrediant 3', '8ingrediant 4', '8ingrediant 5']
Meal_9 = ['name 9', 9, '9ingrediant 1', '9ingrediant 2', '9ingrediant 3', '9ingrediant 4', '9ingrediant 5']
Meal_10 = ['name 10', 10, '10ingrediant 1', '10ingrediant 2', '10ingrediant 3', '10ingrediant 4', '10ingrediant 5']
Meal_11 = ['name 11', 11, '11ingrediant 1', '11ingrediant 2', '11ingrediant 3', '11ingrediant 4', '11ingrediant 5']
Meal_12 = ['name 12', 12, '12ingrediant 1', '12ingrediant 2', '12ingrediant 3', '12ingrediant 4', '12ingrediant 5']
Meal_13 = ['name 13', 13, '12ingrediant 1', '12ingrediant 2', '12ingrediant 3', '12ingrediant 4', '12ingrediant 5']
Meal_14 = ['name 14', 14, '13ingrediant 1', '13ingrediant 2', '13ingrediant 3', '13ingrediant 4', '13ingrediant 5']
# if you add more ingrediants add to this too. it tells it what to print in the ingrediant list later(also make sure all the lists are the same lengths)
ingrediant_locations = [2,3,4,5,6]

Meal_name_list = [Meal_1[0], Meal_2[0], Meal_3[0], Meal_4[0], Meal_5[0], Meal_6[0], Meal_7[0], Meal_8[0], Meal_9[0], Meal_10[0], Meal_11[0], Meal_12[0], Meal_13[0], Meal_14[0]]
Meal_cost_list = [Meal_1[1], Meal_2[1], Meal_3[1], Meal_4[1], Meal_5[1], Meal_6[1], Meal_7[1], Meal_8[1], Meal_9[1], Meal_10[1], Meal_11[1], Meal_12[1], Meal_13[1], Meal_14[1]]

#Picking random meals not reapeating
random_1 = random.randint(0, 13)
random_2 = random.randint(0, 13)
while random_2 == random_1:
    random_2 = random.randint(0, 13)
random_3 = random.randint(0, 13)
while random_3 == random_2 or random_3 == random_1:
    random_3 = random.randint(0, 13)
random_4 = random.randint(0, 13)
while random_4 == random_3 or random_4 == random_2 or random_4 == random_1:
    random_4 = random.randint(0, 13)
random_5 = random.randint(0, 13)
while random_5 == random_4 or random_5 == random_3 or random_5 == random_2 or random_5 == random_1:
    random_5 = random.randint(0, 13)

#calculates cost
cost = Meal_cost_list[random_1] + Meal_cost_list[random_2] + Meal_cost_list[random_3] + Meal_cost_list[random_4] + Meal_cost_list[random_5]

#prints info except ingrediants
print('This week we will have', str(Meal_name_list[random_1]) + ',', str(Meal_name_list[random_2]) + ',', str(Meal_name_list[random_3]) + ',' , str(Meal_name_list[random_4]) + ', and', Meal_name_list[random_5])
print('It will cost $' + str(cost))
print('\nIngrediants to buy:')

#prints ingrediants
if random_1 ==0 or random_2 ==0 or random_3 == 0 or random_4 == 0 or random_5 == 0:
    for index in ingrediant_locations:
        print(Meal_1[index])
if random_1 == 1 or random_2 == 1 or random_3 == 1 or random_4 == 1 or random_5 == 1:
    for index in ingrediant_locations:
        print(Meal_2[index])
if random_1 == 2 or random_2 == 2 or random_3 == 2 or random_4 == 2 or random_5 == 2:
    for index in ingrediant_locations:
        print(Meal_3[index])
if random_1 == 3 or random_2 == 3 or random_3 == 3 or random_4 == 3 or random_5 == 3:
    for index in ingrediant_locations:
        print(Meal_4[index])
if random_1 == 4 or random_2 == 4 or random_3 == 4 or random_4 == 4 or random_5 == 4:
    for index in ingrediant_locations:
        print(Meal_5[index])
if random_1 == 5 or random_2 == 5 or random_3 == 5 or random_4 == 5 or random_5 == 5:
    for index in ingrediant_locations:
        print(Meal_6[index])
if random_1 == 6 or random_2 == 6 or random_3 == 6 or random_4== 6 or random_5 == 6:
    for index in ingrediant_locations:
        print(Meal_7[index])
if random_1 == 7 or random_2 == 7 or random_3 == 7 or random_4 == 7 or random_5 == 7:
    for index in ingrediant_locations:
        print(Meal_8[index])
if random_1 == 8 or random_2 == 8 or random_3 == 8 or random_4 == 8 or random_5 == 8:
    for index in ingrediant_locations:
        print(Meal_9[index])
if random_1 == 9 or random_2 == 9 or random_3 == 9 or random_4 == 9 or random_5 == 9:
    for index in ingrediant_locations:
        print(Meal_10[index])
if random_1 == 10 or random_2 == 10 or random_3 == 10 or random_4 == 10 or random_5 == 10:
    for index in ingrediant_locations:
        print(Meal_11[index])
if random_1 == 11 or random_2 == 11 or random_3 == 11 or random_4 == 11 or random_5 == 11:
    for index in ingrediant_locations:
        print(Meal_12[index])
if random_1 == 12 or random_2 == 12 or random_3 == 12 or random_4 == 12 or random_5 == 12:
    for index in ingrediant_locations:
        print(Meal_13[index])
if random_1 == 13 or random_2 == 13 or random_3 == 13 or random_4 == 13 or random_5 == 13:
    for index in ingrediant_locations:
        print(Meal_14[index])
