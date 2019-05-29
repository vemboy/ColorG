# Libraries
import re
import math
import itertools
from PIL import Image
from collections import Counter
from urllib.parse import urlencode
from urllib.request import urlretrieve
amount = 50
# Functions

def screenshotting_pic():
    params = urlencode(dict(access_key="84f153a9b9424f1cb562b9d3fc66347e",
                        url="https://google.com",
                        full_page=True))
    urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "screenshot_api_example.jpeg")
    print("Done!")

    
def open_image(local_url):
    the_image = Image.open(local_url)

    colors = the_image.getcolors(the_image.size[0]*the_image.size[1])
    return colors
    
def cleaning_list(lst):
    
    o = 1

    while(o < len(lst)):
        if(o % 4 == 0):
            print("deleted " + str(lst[o]))
            del lst[o]
            
        
        o = o + 1

    clean_list = lst
    return clean_list
    
    

def dictionizing(lst):


    color_dict = {

    }

    
    color_usage_dict = {

    }

    o = 1
    counter = 0

    while(o < len(lst)):
        
        
        if(o % 4 == 0):
            counter = counter + 1
            color_RGB = [lst[o - 3], lst[o - 2], lst[o - 1]]
            color_dict['color_' + str(counter)] = color_RGB
            color_usage_dict['color_' + str(counter)] = lst[o - 4]
            
        o = o + 1

    dict_list = [color_dict, color_usage_dict]
    return dict_list




def rgb2lab ( inputColor ) :

   num = 0
   RGB = [0, 0, 0]

   for value in inputColor :
       value = float(value) / 255

       if value > 0.04045 :
           value = ( ( value + 0.055 ) / 1.055 ) ** 2.4
       else :
           value = value / 12.92

       RGB[num] = value * 100
       num = num + 1

   XYZ = [0, 0, 0,]

   X = RGB [0] * 0.4124 + RGB [1] * 0.3576 + RGB [2] * 0.1805
   Y = RGB [0] * 0.2126 + RGB [1] * 0.7152 + RGB [2] * 0.0722
   Z = RGB [0] * 0.0193 + RGB [1] * 0.1192 + RGB [2] * 0.9505
   XYZ[ 0 ] = round( X, 4 )
   XYZ[ 1 ] = round( Y, 4 )
   XYZ[ 2 ] = round( Z, 4 )

   XYZ[ 0 ] = float( XYZ[ 0 ] ) / 95.047         # ref_X =  95.047   Observer= 2°, Illuminant= D65
   XYZ[ 1 ] = float( XYZ[ 1 ] ) / 100.0          # ref_Y = 100.000
   XYZ[ 2 ] = float( XYZ[ 2 ] ) / 108.883        # ref_Z = 108.883

   num = 0
   for value in XYZ :

       if value > 0.008856 :
           value = value ** ( 0.3333333333333333 )
       else :
           value = ( 7.787 * value ) + ( 16 / 116 )

       XYZ[num] = value
       num = num + 1

   Lab = [0, 0, 0]

   L = ( 116 * XYZ[ 1 ] ) - 16
   a = 500 * ( XYZ[ 0 ] - XYZ[ 1 ] )
   b = 200 * ( XYZ[ 1 ] - XYZ[ 2 ] )

   Lab [ 0 ] = round( L, 4 )
   Lab [ 1 ] = round( a, 4 )
   Lab [ 2 ] = round( b, 4 )

   return Lab


def distance_calculator_2by2(color_list):
    
    counter = 0
    color_reset = 0
    loop_runner = 0
    color_name_counter = 1
    avarage_counter = 0

    color1 = [] 
    color2 = []
    distance_avarage = 0
    

    while(loop_runner < amount):
        print("========")
        print("========")
        print("Run: " + str(counter) + " ALSO color difference: " + str(counter) + " the shit is " + str(counter % 2))
        print("========") 
        print("========")

        if(counter == 0):
            print("code passed")
            pass

        if(color_reset == 2):
            print("calculating avarage ---------")
            print("color1: " + str(color1))
            print("color2: " + str(color2))
            lab_color1 = rgb2lab(color1)
            lab_color2 = rgb2lab(color2)
            print("Color1_LAB:" + str(lab_color1))
            print("Color2_LAB:" + str(lab_color2))
            print(math.sqrt((lab_color1[0]-lab_color2[0])**2 + (lab_color1[1]-lab_color2[1])**2 + (lab_color1[2]-lab_color2[2])**2))
            print("calculating avarage ---------")
            distance_avarage = distance_avarage + math.sqrt((lab_color1[0]-lab_color2[0])**2 + (lab_color1[1]-lab_color2[1])**2 + (lab_color1[2]-lab_color2[2])**2)
            color1 = []
            color2 = []
            color_reset = 0
            avarage_counter = avarage_counter + 1


        elif(counter % 2 == 0):
                
                color_reset = color_reset + 1
                color1 = color_list[0]['color_' + str(color_name_counter)]
                print("THIS IS COLOR 1: " + str(color1))
                print("this is colornamecounter: " + str(color_name_counter))
                color_name_counter = color_name_counter + 1
                
                    
        elif(counter % 2 == 1):

                color_reset = color_reset + 1
                color2 = color_list[0]['color_' + str(color_name_counter)]
                print("THIS IS COLOR 2: " + str(color2))
                print("this is colornamecounter: " + str(color_name_counter))
                color_name_counter = color_name_counter + 1

        
        loop_runner = loop_runner + 1
        counter = counter + 1

    distance_avarage = distance_avarage / avarage_counter
    
    return distance_avarage


def distance(color1,color2):
    the_distance = math.sqrt((color1[0] - color2[0])**2 + (color1[1] - color2[1])**2 + (color1[2] - color2[2])**2)
    print("DOING LAB DISTANCE ___________")
    print(str(the_distance))
    print("FINISHED LAB DISTANCE _________")
    return the_distance  

def distance_calculator_1forall(color_list):

    color_name_counter = 1
    loop_runner = 0
    colors = []
    color_distances = []
    total = 0
    total_avarage = 0

    while(loop_runner < amount):
        
        color = color_list[0]['color_' + str(color_name_counter)]
        color_lab = rgb2lab(color)
        colors.append(color_lab)
        
        color_name_counter = color_name_counter + 1
        loop_runner = loop_runner + 1

    for i in range(len(colors)):
        for j in range(i + 1, len(colors)):
            color_distances.append(distance(colors[i], colors[j]))

    for items in range(0, len(color_distances)): 
        total = total + color_distances[items]
        total_avarage = total/len(color_distances)



    return total_avarage
                                                                                #Delta E	Perception
                                                                                #<= 1.0	Not perceptible by human eyes.
                                                                                #1 - 2	Perceptible through close observation.
                                                                                #2 - 10	Perceptible at a glance.
                                                                                #11 - 49	Colors are more similar than opposite
                                                                                #100	Colors are exact opposite
def define_distance(distance):

    distance_defention = ""

    if(distance <= 1):
        distance_defention = "Not perceptible by human eyes. (Color combination complexity)"
    elif(distance > 1 and distance < 2):
        distance_defention = "Perceptible through close observation. (Color combination complexity)"
    elif(distance > 2 and distance < 10):
        distance_defention = "Perceptible at a glance. (Color combination complexity)"
    elif(distance > 10 and distance < 50):
        distance_defention = "Colors are more similar than opposite (Color combination complexity)"
    elif(distance > 50):
        distance_defention = "Colors are exact opposite (Color combination complexity)"

    return distance_defention
        
avarage_list_2by2 = []
avarage_list_1forall = []

def avarage_of_avarages42(avarage):
    
    
    avarage_list_2by2.append(avarage)
    return avarage_list_2by2

def avarage_of_avarages4all(avarage):
    avarage_list_1forall.append(avarage)
    return avarage_list_1forall

def sum_avarage(avarage_list):
    true_avarage = sum(avarage_list) / len(avarage_list)
    return true_avarage