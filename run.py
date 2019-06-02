from color_sourcer import open_image, cleaning_list, dictionizing, distance_calculator_2by2, distance_calculator_1forall, amount, define_distance, avarage_list_2by2, avarage_list_1forall, avarage_of_avarages42, avarage_of_avarages4all, sum_avarage

from collections import Counter
import re


# Opening the image (locally)
number_of_pics = 10
i = 1
while(i <=   number_of_pics):

    colors = open_image("C:\\Users\\vemboy\\Documents\\GitHub\\Color-Guerdon\\saved_images\\low_distance\\aesthetic{}.jpg".format(str(i)))

    # Top colors 
    counter = Counter(colors)
    counter_list = re.findall(r'\d+', str(counter.most_common(amount + 1)))

    # Cleaning list
    clean_list = cleaning_list(counter_list)

    # Putting list into a dictionary ( most common - 1 )
    dict_list = dictionizing(clean_list)

    #Finding avarage distance in list by comparing 2 top colors with each other till list finishes ( WITH LAB FORMULA )
    distance_avarage = distance_calculator_2by2(dict_list)

    #Finding the avarage distance in a list by comparing each element with all others ( WITH LAB FORMULA )
    if(amount <= 50):      #50 to not count for too long, combination amount too large
        total_avarage = distance_calculator_1forall(dict_list)
    else:
        pass

    avarage_of_avarages42(distance_avarage)
    avarage_of_avarages4all(total_avarage)
    

    i = i + 1

distance_avarage = sum_avarage(avarage_list_2by2)
total_avarage = sum_avarage(avarage_list_1forall)

avarage_defenition = define_distance(distance_avarage)
total_defenition = define_distance(total_avarage)

# OUTPUT
print("")
print("----AVARAGE----")
print(distance_avarage)
print(avarage_defenition)
print("")
print("----TOTAL----")
print(total_avarage)
print(total_defenition)
print("")
print("----LIST----")
print("")
print("----2by2_method----")
print(avarage_list_2by2)
print("")
print("----1forall_method----")
print(avarage_list_1forall)
print("")
