from tkinter.messagebox import IGNORE


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
    i = 1
    h_room= float(input(f"Enter height of room? (ft/in)#  \n (Standard size: 8.10)# \t".format(i+1)))
    w_room= float(input(f"Enter width of room? (ft/in)#  \n (Standard size: 11.10)# \t ".format(i+1)))
    l_room= float(input(f"Enter length of room? (ft/in)#  \n (Standard size: 12.05)# \t".format(i+1)))
    h_wi_room= float(input(f"Enter height of window in the room if any or press 0? (ft/in)# \n (Standard size: 5.00)# \t".format(i+1)))
    w_wi_room= float(input(f"Enter width of window in the room if any or press 0? (ft/in)# \n (Standard size: 2.60)# \t".format(i+1)))
    h_door_room= float(input(f"Enter height of door in the room if any or press 0? (ft/in)# \n (Standard size: 6.80)# \t".format(i+1)))
    w_door_room= float(input(f"Enter width of door in the room if any or press 0? (ft/in)# \n (Standard size: 2.75)# \t".format(i+1)))
    h_c_room= float(input(f"Enter height of outer mount of closet if any or press 0?(ft/in)# \n (Standard size: 6.10)\t#".format(i+1)))
    w_c_room= float(input(f"Enter width of outer mount of closet if any or press 0?(ft/in)# \n (Standard size: 5.50)\t#".format(i+1)))
    h_s_room= float(input(f"Enter height of socket if any or press 0?(ft/in) \n(Standard size: 0.60)\t#".format(i+1)))
    w_s_room= float(input(f"Enter width of socket if any or press 0?(ft/in)\n(Standard size: 0.60)\t# ".format(i+1)))

    h_room_total = h_room_total+h_room
    w_room_total = w_room_total+w_room
    l_room_total = l_room_total+l_room
    h_wi_room_total = h_wi_room_total + h_wi_room
    w_wi_room_total = w_wi_room_total + w_wi_room
    h_door_room_total = h_door_room_total + h_door_room
    w_door_room_total = w_door_room_total + w_door_room
    h_c_room_total = h_c_room_total + h_c_room
    w_c_room_total = w_c_room_total + w_c_room
    h_s_room_total = h_s_room_total + h_s_room
    w_s_room_total = w_s_room_total + w_s_room

    total_room=((h_room_total*w_room_total)*2)+((h_room_total*l_room_total)*2)
    not_to_paint = (h_wi_room_total+w_wi_room_total+h_door_room_total+w_door_room_total+h_c_room_total+w_c_room_total+h_s_room_total+w_s_room_total)
    total_room=total_room - not_to_paint
    gallon = (total_room/400) * b
    print (f"Total surface area of room is {total_room} sq.ft.")
    print (f"Total surface area of room that don't need paint is {not_to_paint} sq.ft.")
    print (f"Total paint required to paint the room is {gallon} gallons")

wall = (input("Would you like to paint any other walls? \n (y) YES \n (n) NO \n")).lower()
if wall == "y":
    c =int(input("Enter number of Walls#  "))
    d =int(input("Enter number of Coats#  "))
    for j in range(c):
        j = 1
        h_wall= float(input(f"Enter height of wall#  ".format(j+1)))
        w_wall= float(input(f"Enter width of wall#  ".format(j+1)))
        h_wi_wall= float(input(f"Enter height of window in the wall if any or press 0? (ft/in)# \n (Standard size: 5.00) \t#  ".format(i+1)))
        w_wi_wall= float(input(f"Enter width of window in the wall if any or press 0? (ft/in)# \n (Standard size: 2.60) \t#  ".format(i+1)))
        h_door_wall= float(input(f"Enter height of door in the wall if any or press 0? (ft/in)# \n (Standard size: 6.80) \t#  ".format(i+1)))
        w_door_wall= float(input(f"Enter width of door in the wall if any or press 0? (ft/in)# \n (Standard size: 2.75) \t#  ".format(i+1)))
        h_c_wall= float(input(f"Enter height of outer mount of closet if any or press 0?(ft/in)# \n (Standard size: 6.10)\t#  ".format(i+1)))
        w_c_wall= float(input(f"Enter width of outer mount of closet if any or press 0?(ft/in)# \n (Standard size: 5.50)\t#  ".format(i+1)))
        h_s_wall= float(input(f"Enter height of socket if any or press 0?(ft/in) \n(Standard size: 0.60)\t#  ".format(i+1)))
        w_s_wall= float(input(f"Enter width of socket if any or press 0?(ft/in)\n(Standard size: 0.60)\t#  ".format(i+1)))

        h_wall_total = h_wall_total+h_wall
        w_wall_total = w_wall_total+w_wall
        h_wi_wall_total = h_wi_wall_total + h_wi_wall
        w_wi_wall_total = w_wi_wall_total + w_wi_wall
        h_door_wall_total = h_door_wall_total + h_door_wall
        w_door_wall_total = w_door_wall_total + w_door_wall
        h_c_wall_total = h_c_wall_total + h_c_wall
        w_c_wall_total = w_c_wall_total + w_c_wall
        h_s_wall_total = h_s_wall_total + h_s_wall
        w_s_wall_total = w_s_wall_total + w_s_wall


        total_wall=(h_wall_total*w_wall_total)
        not_to_paint1 = (h_wi_wall_total+w_wi_wall_total+h_door_wall_total+w_door_wall_total+h_c_wall_total+w_c_wall_total+h_s_wall_total+w_s_wall_total)
        total_wall=total_wall - not_to_paint
        gallon1 = (total_wall/400) * b
        print (f"Total surface area of wall is                               :     {total_wall} sq.ft.")
        print(f"Total surface area for both room and walls                   :     {total_room + total_wall} sq.ft")
        print (f"Total surface area of wall that don't need paint            :     {not_to_paint1} sq.ft.")
        print(f"Total surface area of wall and room that don't need paint    :     {not_to_paint + not_to_paint1} sq.ft")
        print (f"Total paint required to paint the walls is                  :      {gallon1} gallons")
        print(f" Total gallons to paint                                      :      {gallon + gallon1}")

elif wall =="n":
    TOTAL = TOTAL + total_room + total_wall
    GALLON = GALLON + gallon + gallon1
    not_to_paint1 = (h_wi_wall_total+w_wi_wall_total+h_door_wall_total+w_door_wall_total+h_c_wall_total+w_c_wall_total+h_s_wall_total+w_s_wall_total)
    TOTAL = TOTAL - (not_to_paint1 + not_to_paint)
    print (f"\tTotal surface area of (rooms+walls) is {TOTAL} sq.ft.")
    print (f"Total surface area of room that don't need paint is {not_to_paint + not_to_paint1} sq.ft.")
    print (f"\tTotal paint required for entire unit/house is {GALLON} gallons.")

else:
    print ("Invalid entry, TRY AGAIN")
    TOTAL = TOTAL + total_room + total_wall
    GALLON = GALLON + gallon + gallon1
    not_to_paint1 = (h_wi_wall_total+w_wi_wall_total+h_door_wall_total+w_door_wall_total+h_c_wall_total+w_c_wall_total+h_s_wall_total+w_s_wall_total)
    TOTAL = TOTAL - (not_to_paint1 + not_to_paint)
    print ("\t-----------TOTAL PAINT REQUIRED-----------")
    print (f"Total surface area of (rooms+walls) is {TOTAL} sq.ft.")
    print (f"Total surface area of room that don't need paint is {not_to_paint + not_to_paint1} sq.ft.")
    print (f"Total paint required to paint the entire unit/house is {GALLON} gallons")


print("________________________________________________________")
print("Select the type of color brand you want according to your budget and deals preferred!!")

   

brand= [["The Colonies \n4.5 stars \nloyalty disciunt 15% \nNo shipping cost ",30.00,"gallons"],
   ["BEHR-Premium \n5 stars \nNo discount \nshipping cost $10 ",49.99,"gallons" ],
   ["Asian Paints \n2.5 stars \nNo discount \nshipping cost $10 ",25.49,"gallons"],
   ["Organic Paint \n3 stars \nNo discount \nshipping cost $10",39.99,"gallons"]]

for f in brand:
    print ("{}.".format(brand.index(f)+1),end='')
    print("{:17}${:.2f}".format(f[0],f[1]))

brands=int(input("Choose any one brand from above: "))

def company_details():

   if brands == 1:
    discount = 15/100
    shipping_cost= 0
    gallon_price = 30.00
    newtotal = TOTAL - discount + shipping_cost * gallon_price
    return newtotal

   elif brands==2:
    discount = 0
    shipping_cost= 10
    gallon_price = 49.99
    newtotal = TOTAL - discount + shipping_cost * gallon_price
    return newtotal

   elif brands ==3:
    discount = 0
    shipping_cost= 10
    gallon_price = 25.49
    newtotal = TOTAL - discount + shipping_cost * gallon_price
    return newtotal

   elif brands ==4:
    discount = 0
    shipping_cost= 10
    gallon_price = 39.99
    newtotal = TOTAL - discount + shipping_cost * gallon_price
    return newtotal

   else:
    print("**** Please select any one brand!!")
    company_details()


print("-------------SUMMARY------------")
print(f"Total sqft:            {TOTAL}")
print(f"Total gallons:         {GALLON}")
print("Total paint cost:               ",company_details())





    

#def coffee():
    
#    coftype = input ( "\n Enter type of coffee: \n (a)regular \n (b) hazelnut \n (c) pumpkin spice\n: ")
   
#    if coftype == "a":
#        return " Regular coffee."
#    elif coftype =="b":
#        return " Hazelnut coffee."
#    elif coftype == "c":
#        return " Pumpkin spice coffee."
#    else:
#          error_message()
#          return coffee()


