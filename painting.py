print("__________________________________________________________________________________________________________________________")
print ("\t\t\t***WELCOME TO THE COLONIES PAINT- Colouring your dreams to Reality***\t")
print("__________________________________________________________________________________________________________________________")


# Calculate how much paint user needs to buy?

h_wall_total=0
w_wall_total=0
h_room_total=0
w_room_total=0
l_room_total=0
total_room=0
total_wall=0
TOTAL=0
gallon=0
gallon1=0
GALLON=0
h_wi_room_total = 0
w_wi_room_total = 0
h_door_room_total =0
w_door_room_total = 0
h_c_room_total =0
w_c_room_total = 0
h_s_room_total = 0
w_s_room_total = 0
h_wi_wall_total=0
w_wi_wall_total=0
h_door_wall_total=0
w_door_wall_total =0
h_c_wall_total = 0
w_c_wall_total = 0
h_s_wall_total = 0
w_s_wall_total = 0
not_to_paint1=0
not_to_paint=0
discount = 0
shipping_cost= 0
gallon_price = 0
newtotal=0
TOTAL_AGG=0
not_to_paint_TOTAL=0
raw_input=0
Total_cost=0
#def total_room(h_room_total,l_room_total,w_room_total,gallon):
#    total_room=((h_room_total*w_room_total)*2)+((h_room_total*l_room_total)*2)
#    gallon = (total_room/400) * b
#    print (f"Total surface area of room is {total_room} sq.ft.")
#    print (f"Total paint required to paint the room is {gallon} gallons")
#    return

#def total_wall(h_wall_total,w_wall_total,gallon1):
#    total_wall=(h_wall_total*w_wall_total)
#    gallon1 = (total_wall/400) * b
#    print (f"Total surface area of wall is {total_wall} sq.ft.")
#    print (f"Total paint required to paint the room is {gallon1} gallons")
#    return

#def TOTAL (total_room,total_wall):
#    TOTAL = TOTAL + total_room + total_wall
#    return

#def GALLON (gallon,gallon1):
#    GALLON = GALLON + gallon + gallon1
#    return



a =int(input("Enter number of Rooms#  "))
b =int(input("Enter number of Coats#  "))

for i in range(a):
    h_room= float(input(f"Enter height of room? (ft/in)#  \n (Standard size: 8.10)# \n#  "))
    w_room= float(input(f"Enter width of room? (ft/in)#  \n (Standard size: 11.10)# \n#  "))
    l_room= float(input(f"Enter length of room? (ft/in)#  \n (Standard size: 12.05)# \n#  "))
    h_wi_room= float(input(f"Enter height of outer mount of window in the room if any or press 0? (ft/in)# \n (Standard size: 5.00)# \n#  "))
    w_wi_room= float(input(f"Enter width of outer mount of window in the room if any or press 0? (ft/in)# \n (Standard size: 2.60)# \n#  "))
    h_door_room= float(input(f"Enter height of door in the room if any or press 0? (ft/in)# \n (Standard size: 6.80)# \n#  "))
    w_door_room= float(input(f"Enter width of door in the room if any or press 0? (ft/in)# \n (Standard size: 2.75)# \n#  "))
    h_c_room= float(input(f"Enter height of outer mount of closet if any or press 0?(ft/in)# \n (Standard size: 6.10)# \n#  "))
    w_c_room= float(input(f"Enter width of outer mount of closet if any or press 0?(ft/in)# \n (Standard size: 5.50)# \n#  "))
    h_s_room= float(input(f"Enter height of socket if any or press 0?(ft/in) \n(Standard size: 0.60)# \n#  "))
    w_s_room= float(input(f"Enter width of socket if any or press 0?(ft/in)\n(Standard size: 0.60)# \n#  "))

    h_room_total = h_room_total+h_room
    w_room_total = w_room_total+w_room
    l_room_total = l_room_total+l_room
    h_wi_room_total = h_wi_room_total + h_wi_room
    w_wi_room_total = w_wi_room_total + w_wi_room
    area_wi_room_total = (h_wi_room_total*w_wi_room_total)
    h_door_room_total = h_door_room_total + h_door_room
    w_door_room_total = w_door_room_total + w_door_room
    area_door_room_total = (h_door_room_total*w_door_room_total)
    h_c_room_total = h_c_room_total + h_c_room
    w_c_room_total = w_c_room_total + w_c_room
    area_c_room_total = (h_c_room_total*w_c_room_total)
    h_s_room_total = h_s_room_total + h_s_room
    w_s_room_total = w_s_room_total + w_s_room
    area_s_room_total = (h_s_room_total*w_s_room_total)

    total_room=(h_room_total*w_room_total)+(h_room_total*l_room_total)+(l_room_total*w_room_total)
    not_to_paint = (area_wi_room_total+area_door_room_total+area_c_room_total+area_s_room_total)
    total_room=total_room - not_to_paint
    gallon = (total_room/400) * b
    print("-----------------------------------TOTAL PAINT REQUIRED--------------------------------------------------------------")
    print (f"Total surface area of room is                        :        {total_room:.2f} sq.ft.")
    print (f"Total surface area of room that don't need paint is  :        {not_to_paint:.2f} sq.ft.")
    print (f"Total paint required to paint the room is            :         {gallon:.2f} gallons")
    print("__________________________________________________________________________________________________________________________")


wall = (input("Would you like to paint any other walls? \n (y) YES \n (n) NO \n")).lower()
if wall == "y":
    c =int(input("Enter number of Walls#  "))
    d =int(input("Enter number of Coats#  "))
    for j in range(c):
        h_wall= float(input(f"Enter height of wall#  "))
        w_wall= float(input(f"Enter width of wall#  "))
        h_wi_wall= float(input(f"Enter height of window in the wall if any or press 0? (ft/in)# \n (Standard size: 5.00) \n#  "))
        w_wi_wall= float(input(f"Enter width of window in the wall if any or press 0? (ft/in)# \n (Standard size: 2.60) \n#  "))
        h_door_wall= float(input(f"Enter height of door in the wall if any or press 0? (ft/in)# \n (Standard size: 6.80) \n#  "))
        w_door_wall= float(input(f"Enter width of door in the wall if any or press 0? (ft/in)# \n (Standard size: 2.75) \n#  "))
        h_c_wall= float(input(f"Enter height of outer mount of closet if any or press 0?(ft/in)# \n (Standard size: 6.10)\n#  "))
        w_c_wall= float(input(f"Enter width of outer mount of closet if any or press 0?(ft/in)# \n (Standard size: 5.50)\n#  "))
        h_s_wall= float(input(f"Enter height of socket if any or press 0?(ft/in) \n(Standard size: 0.60)\n#  "))
        w_s_wall= float(input(f"Enter width of socket if any or press 0?(ft/in)\n(Standard size: 0.60)\n#  "))

        h_wall_total = h_wall_total+h_wall
        w_wall_total = w_wall_total+w_wall
        h_wi_wall_total = h_wi_wall_total + h_wi_wall
        w_wi_wall_total = w_wi_wall_total + w_wi_wall
        area_wi_wall_total = (h_wi_wall_total*w_wi_wall_total)
        h_door_wall_total = h_door_wall_total + h_door_wall
        w_door_wall_total = w_door_wall_total + w_door_wall
        area_door_wall_total = (h_door_wall_total*w_door_wall_total)
        h_c_wall_total = h_c_wall_total + h_c_wall
        w_c_wall_total = w_c_wall_total + w_c_wall
        area_c_wall_total = (h_c_wall_total*w_c_wall_total)
        h_s_wall_total = h_s_wall_total + h_s_wall
        w_s_wall_total = w_s_wall_total + w_s_wall
        area_s_wall_total = (h_s_wall_total*w_s_wall_total)

        total_wall=(h_wall_total*w_wall_total)
        not_to_paint1 = (area_wi_wall_total+area_door_wall_total+area_c_wall_total+area_s_wall_total)
        total_wall=total_wall - not_to_paint1
        gallon1 = (total_wall/400) * b


        print("----------------------------------------TOTAL PAINT REQUIRED---------------------------------------------------------")
        print (f"Total surface area of wall is                               :     {total_wall:.2f} sq.ft.")
        print(f"Total surface area for both room and walls                   :     {total_room + total_wall:.2f} sq.ft")
        print (f"Total surface area of wall that don't need paint            :     {not_to_paint1:.2f} sq.ft.")
        print(f"Total surface area of wall and room that don't need paint    :     {not_to_paint + not_to_paint1:.2f} sq.ft")
        print (f"Total paint required to paint the walls is                  :      {gallon1:.2f} gallons")
        print(f" Total paint required to paint wall and room is              :      {gallon + gallon1:.2f} gallons")
        print("__________________________________________________________________________________________________________________________")


        TOTAL = TOTAL + total_room + total_wall # sq./ft
        GALLON = GALLON + gallon + gallon1
        not_to_paint_TOTAL = not_to_paint_TOTAL+not_to_paint+not_to_paint1
        TOTAL_AGG = TOTAL - not_to_paint_TOTAL

elif wall =="n":
    TOTAL = TOTAL + total_room + total_wall
    GALLON = GALLON + gallon + gallon1
    not_to_paint_TOTAL = not_to_paint+not_to_paint1
    TOTAL_AGG = TOTAL - not_to_paint_TOTAL
    print("---------------------------------------TOTAL PAINT REQUIRED----------------------------------------------------------")
    print (f"Total surface area of rooms to paint is                :     {TOTAL_AGG:.2f} sq.ft.")
    print (f"Total surface area of room that don't need paint is    :     {not_to_paint_TOTAL:.2f} sq.ft.")
    print (f"Total paint required for entire unit is                :     {GALLON:.2f} gallons.")
    print("__________________________________________________________________________________________________________________________")


else:
    print ("Invalid entry, TRY AGAIN")
    TOTAL = TOTAL + total_room + total_wall
    GALLON = GALLON + gallon + gallon1
    not_to_paint_TOTAL = not_to_paint_TOTAL+not_to_paint+not_to_paint1
    TOTAL_AGG = TOTAL - not_to_paint_TOTAL
    print("---------------------------------------TOTAL PAINT REQUIRED----------------------------------------------------------")
    print (f"Total surface area of (rooms+walls) to paint is                 :    {TOTAL_AGG:.2f} sq.ft.")
    print (f"Total surface area of room that don't need paint is             :    {not_to_paint_TOTAL:.2f} sq.ft.")
    print (f"Total paint required to paint the entire unit/house is          :     {GALLON:.2f} gallons")
    print("__________________________________________________________________________________________________________________________")


print("__________________________________________________________________________________________________________________________")
print("Select the brand of paint you wish to buy based on your budget and preferred DEALS!!")
print("__________________________________________________________________________________________________________________________")


brand = [
    ["The Colonies ==>", 30.00," per gallon \n\t\t => 4.5 stars \n\t ========>>> SPECIAL Loyalty discount 15% <<<======== \n\t\t =>No shipping cost \n\t\t\t "], #=> 1. Mocha Light \n 2. Aqua Fresco \n 3. Healing Aloe \n\t\t\t
   ["BEHR-Premium ==>" ,49.99," per gallon \n\t\t => 5 stars \n\t\t => No discount \n\t\t => Shipping cost $10 \n\t\t\t "], #=> 1. Copper Patina \n 2. White Pearl \n 3. Purple \n\t\t\t
   ["Asian Paints ==>",25.49," per gallon \n\t\t => 2.5 stars \n\t\t => No discount \n\t\t => Shipping cost $10 \n\t\t\t "], #=> 1. Black \n 2. Mocha Light \n 3. Blue
   ["Organic Paint ==>",39.99," per gallon \n\t\t => 3 stars \n\t\t => Loyalty discount 10% \n\t\t => Shipping cost $10 \n\t\t\t ",]] # => 1. White \n 2. Aqua Fresco \n 3. Orange \n\t\t\t
 
for f in brand:
    print ("{}.".format(brand.index(f)+1),end='')
    print("{}${:.2f}{}".format(f[0],f[1],f[2]))
brands=int(input("Choose any one brand from above: "))


GALLON = round(gallon + gallon1)
not_to_paint_TOTAL = (not_to_paint+not_to_paint1)
TOTAL = (total_room+total_wall)
TOTAL_AGG = TOTAL-not_to_paint_TOTAL

#brands=int(input("Choose any one brand from above: "))
def error_message():
    error= print ("Input correct value! ERROR !!")
    return error
'''
#def company_select():
    match brands:
        case 1:
            #print("The Colonies")
        case 2:
            #print ("BEHR-Premium")
        case 3:
            #print ("Asian Paints")   
        case 4:
            #print("Organic Paint")
        #case _:
            #error_message()
            #return company_select()
'''
#company_select()
# Colonies: 1. Mocha Light (+1) \n 2. Aqua Fresco (+2) \n 3. Healing Aloe (+3) => $30
# BEHR: 1. Copper Patina (+1) \n 2. White Pearl (+3) \n 3. Purple (+1.5) =>$49.99
# Asian Paints: 1. Black (+0.5) \n 2. Mocha Light (+1) \n 3. Blue (+2) => $25.49
# Organic Paint: 1. White (+1.5) \n 2. Aqua Fresco (+2) \n 3. Orange (+1) => $39.99

color_num = 0
match brands:
    case 1:
        print("The Colonies")
        color_num= int(input(" Choose color of paint\n 1. Mocha Light ($31 per gallon) \n 2. Aqua Fresco ($32 per gallon) \n 3. Healing Aloe ($33 per gallon)\n ==>  ")) 
    
    case 2:
        print ("BEHR-Premium")
        color_num= int(input(" Choose color of paint\n 1. Copper Patina ($50.99 per gallon) \n 2. Healing Aloe ($52.99 per gallon) \n 3. Purple ($51.49 per gallon)\n ==>  "))
    
    case 3:
        print ("Asian Paints") 
        color_num= int(input("Choose color of marigold\n 1. Black ($26.99 per gallon) \n 2. Mocha Light  ($26.49 per gallon) \n 3. Blue ($27.49 per gallon) \n ==>  "))
    
    case 4:
        print("Organic Paint")
        color_num= int(input("Choose color of lilies\n  1. White ($41.49 per gallon) \n 2. Aqua Fresco ($41.99 per gallon) \n 3. Orange ($40.99 per gallon) \n ==>  ")) 
     
    case _:
        print("Please choose correct color!")

print (f"You have selected Color# {color_num} from Company# {brands}")

# Colonies: 1. Mocha Light (+1) \n 2. Aqua Fresco (+2) \n 3. Healing Aloe (+3)
# BEHR: 1. Copper Patina (+1) \n 2. White Pearl (+3) \n 3. Purple (+1.5)
# Asian Paints: 1. Black (+1.5) \n 2. Mocha Light (+1) \n 3. Blue (+2)
# Organic Paint: 1. White (+1.5) \n 2. Aqua Fresco (+2) \n 3. Orange (+1)

def calculation_details():
    if color_num == 1 and brands ==1:
        discount = 15/100
        shipping_cost= 0
        gallon_price = 31
        newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
        return newtotal
    elif color_num == 2 and brands ==1:
        discount = 15/100
        shipping_cost= 0
        gallon_price = 32
        newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
        return newtotal
    elif color_num== 3 and brands ==1:
        discount = 15/100
        shipping_cost= 0
        gallon_price = 33
        newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
        return newtotal
    elif color_num == 1 and brands ==2:
        discount = 0
        shipping_cost= 10
        gallon_price = 50.99
        newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
        return newtotal
    elif color_num == 2 and brands ==2:
        discount = 0
        shipping_cost= 10
        gallon_price = 52.99
        newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
        return newtotal
    elif color_num == 3 and brands ==2:
        discount = 0
        shipping_cost= 10
        gallon_price = 51.49
        newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
        return newtotal
    elif color_num == 1 and brands ==3:
        discount = 0
        shipping_cost= 10
        gallon_price = 26.99
        newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
        return newtotal
    elif color_num == 2 and brands ==3:
        discount = 0
        shipping_cost= 10
        gallon_price = 26.49 
        newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
        return newtotal
    elif color_num == 3 and brands ==3:
        discount = 0
        shipping_cost= 10
        gallon_price = 27.49 
        newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
        return newtotal
    elif color_num == 1 and brands ==4:
        discount = 10/100
        shipping_cost= 10
        gallon_price = 41.49 
        newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
        return newtotal
    elif color_num == 2 and brands ==4:
        discount = 10/100
        shipping_cost= 10
        gallon_price = 41.99
        newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
        return newtotal
    elif color_num == 3 and brands ==4:
        discount = 10/100
        shipping_cost= 10
        gallon_price = 40.99 
        newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
        return newtotal 

    else: # color == 4 and company_select >= 5:
        print (f"Try again {error_message()} ")

        
print(f"-------------------------------------------------------------------------------------------------------------\n-------------------------------------------INVOICE OF THE COLONIES-------------------------------------------\n\nTotal cost to paint entire unit====>                            :           ${calculation_details():.2f}")
print(f"Total surface area to paint for entire unit====>                :            {TOTAL_AGG:.2f}")
print(f"Total area that don't need painting for entire unit====>        :            {not_to_paint_TOTAL:.2f}")
print(f"Total gallons of paint to buy====>                              :            {GALLON:.2f}")
print("-------------------------------------------THANK YOU FOR SHOPPING WITH US-------------------------------------------")


