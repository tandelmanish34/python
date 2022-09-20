
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

def error_message():
    print ("\n Please enter correct value!")
    return error_message()



a =int(input("Enter number of Rooms#  "))
b =int(input("Enter number of Coats#  "))

for i in range(a):
    h_room= float(input(f"Enter height of room? (ft/in)#  \n (Standard size: 8.10)# \t"))
    w_room= float(input(f"Enter width of room? (ft/in)#  \n (Standard size: 11.10)# \t "))
    l_room= float(input(f"Enter length of room? (ft/in)#  \n (Standard size: 12.05)# \t"))
    h_wi_room= float(input(f"Enter height of outer mount of window in the room if any or press 0? (ft/in)# \n (Standard size: 5.00)# \t"))
    w_wi_room= float(input(f"Enter width of outer mount of window in the room if any or press 0? (ft/in)# \n (Standard size: 2.60)# \t"))
    h_door_room= float(input(f"Enter height of door in the room if any or press 0? (ft/in)# \n (Standard size: 6.80)# \t"))
    w_door_room= float(input(f"Enter width of door in the room if any or press 0? (ft/in)# \n (Standard size: 2.75)# \t"))
    h_c_room= float(input(f"Enter height of outer mount of closet if any or press 0?(ft/in)# \n (Standard size: 6.10)# \t"))
    w_c_room= float(input(f"Enter width of outer mount of closet if any or press 0?(ft/in)# \n (Standard size: 5.50)# \t"))
    h_s_room= float(input(f"Enter height of socket if any or press 0?(ft/in) \n(Standard size: 0.60)# \t"))
    w_s_room= float(input(f"Enter width of socket if any or press 0?(ft/in)\n(Standard size: 0.60)# \t "))

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
        h_wi_wall= float(input(f"Enter height of window in the wall if any or press 0? (ft/in)# \n (Standard size: 5.00) \t#  "))
        w_wi_wall= float(input(f"Enter width of window in the wall if any or press 0? (ft/in)# \n (Standard size: 2.60) \t#  "))
        h_door_wall= float(input(f"Enter height of door in the wall if any or press 0? (ft/in)# \n (Standard size: 6.80) \t#  "))
        w_door_wall= float(input(f"Enter width of door in the wall if any or press 0? (ft/in)# \n (Standard size: 2.75) \t#  "))
        h_c_wall= float(input(f"Enter height of outer mount of closet if any or press 0?(ft/in)# \n (Standard size: 6.10)\t#  "))
        w_c_wall= float(input(f"Enter width of outer mount of closet if any or press 0?(ft/in)# \n (Standard size: 5.50)\t#  "))
        h_s_wall= float(input(f"Enter height of socket if any or press 0?(ft/in) \n(Standard size: 0.60)\t#  "))
        w_s_wall= float(input(f"Enter width of socket if any or press 0?(ft/in)\n(Standard size: 0.60)\t#  "))

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
    print (f"Total surface area of rooms is                         :     {TOTAL_AGG:.2f} sq.ft.")
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
    print (f"Total surface area of (rooms+walls) is                          :    {TOTAL_AGG:.2f} sq.ft.")
    print (f"Total surface area of room that don't need paint is             :    {not_to_paint_TOTAL:.2f} sq.ft.")
    print (f"Total paint required to paint the entire unit/house is          :     {GALLON:.2f} gallons")
    print("__________________________________________________________________________________________________________________________")


print("__________________________________________________________________________________________________________________________")
print("Select the brand of paint you wish to buy based on your budget and preferred DEALS!!")
print("__________________________________________________________________________________________________________________________")


brand = [
    ["The Colonies ==>", 30.00," per gallon \n\t\t => 4.5 stars \n\t ========>>> SPECIAL Loyalty discount 15% <<<======== \n\t\t =>No shipping cost \n\t\t\t "],
   ["BEHR-Premium ==>" ,49.99," per gallon \n\t\t => 5 stars \n\t\t => No discount \n\t\t => Shipping cost $10 \n\t\t\t "],
   ["Asian Paints ==>",25.49," per gallon \n\t\t => 2.5 stars \n\t\t => No discount \n\t\t => Shipping cost $10 \n\t\t\t "],
   ["Organic Paint ==>",39.99," per gallon \n\t\t => 3 stars \n\t\t => Loyalty discount 10% \n\t\t => Shipping cost $10 \n\t\t\t ",]]
 
for f in brand:
    print ("{}.".format(brand.index(f)+1),end='')
    print("{}${:.2f}{}".format(f[0],f[1],f[2]))

def error_message():
    error= print ("Input correct value! ERROR !!")
    return error


GALLON = round(gallon + gallon1)
not_to_paint_TOTAL = (not_to_paint+not_to_paint1)
TOTAL = (total_room+total_wall)
TOTAL_AGG = TOTAL-not_to_paint_TOTAL

#brands=int(input("Choose any one brand from above: "))

def company_details():
    brands=int(input("Choose any one brand from above: "))
    match brands:
        case 1:
            discount = 15/100
            shipping_cost= 0
            gallon_price = 30.00
            newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
            return newtotal

        case 2:
       
            discount = 0
            shipping_cost= 10
            gallon_price = 49.99
            newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
            return newtotal
    
        case 3:
        
            discount = 0
            shipping_cost= 10
            gallon_price = 25.49
            newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
            return newtotal
    
        case 4:
       
            discount = 10/100
            shipping_cost= 10
            gallon_price = 39.99
            newtotal = (GALLON * gallon_price)* (1-discount) + shipping_cost
            return newtotal
    
        case _ :
          error_message()
          return company_details()
       
print(f"---------------------------------------------------------------------------------------------------\n-------------------------------------------INVOICE OF THE COLONIES-------------------------------------------\n\nTotal cost to paint entire unit====>                            :           ${company_details():.2f}")
print(f"Total surface area to paint for entire unit====>                :            {TOTAL_AGG:.2f}")
print(f"Total area that don't need painting for entire unit====>        :            {not_to_paint_TOTAL:.2f}")
print(f"Total gallons of paint to buy====>                              :            {GALLON:.2f}")
print("-------------------------------------------THANK YOU FOR SHOPPING WITH US-------------------------------------------")
exit


