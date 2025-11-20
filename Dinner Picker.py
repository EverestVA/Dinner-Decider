import random


#list of meals
Meal_1 = ['name 1', 1, "ingrediant 1", 'ingrediant 2', ]
Meal_2 = ['name 2', 2, "ingrediant 1", 'ingrediant 2', ]
Meal_3 = ['name 3', 3, "ingrediant 1", 'ingrediant 2', ]
Meal_4 = ['name 4', 4, "ingrediant 1", 'ingrediant 2', ]
Meal_5 = ['name 5', 5, "ingrediant 1", 'ingrediant 2', ]
Meal_6 = ['name 6', 6, "ingrediant 1", 'ingrediant 2', ]
Meal_7 = ['name 7', 7, "ingrediant 1", 'ingrediant 2', ]
Meal_8 = ['name 8', 8, "ingrediant 1", 'ingrediant 2', ]
Meal_9 = ['name 9', 9, "ingrediant 1", 'ingrediant 2', ]
Meal_10 = ['name 10', 10, "ingrediant 1", 'ingrediant 2', ]
Meal_11 = ['name 11', 11, "ingrediant 1", 'ingrediant 2', ]
Meal_12 = ['name 12', 12, "ingrediant 1", 'ingrediant 2', ]
Meal_13 = ['name 13', 13, "ingrediant 1", 'ingrediant 2', ]
Meal_14 = ['name 14', 14, "ingrediant 1", 'ingrediant 2', ]

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

cost = Meal_cost_list[random_1] + Meal_cost_list[random_2] + Meal_cost_list[random_3] + Meal_cost_list[random_4] + Meal_cost_list[random_5]
print("This week we will have", Meal_name_list[random_1], Meal_name_list[random_2], Meal_name_list[random_3], Meal_name_list[random_4], Meal_name_list[random_5])
print('It will cost', cost)