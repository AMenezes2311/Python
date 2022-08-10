#Created by Andre Menezes
#with this program you will be able to do the following: Prompt the user to select a shape; Calculate the area of a shape; Print the area of that shape to the user
print "Calculator is starting up"
option = raw_input("Enter C for circle or T for Triangle: ")
if option == "C" or "c":
  radius = float(raw_input("Enter the radius: "))
  area = round(3.14159 * radius ** 2, 2)
  print "Area: %f" % area
elif option == "T" or "t":
  base = float(raw_input("Enter the base: "))
  height = float(raw_input("Enter the height: "))
  area = 0.5 * base * height
  print "Area: %.2f" % area
else:
  print "Enter a valid shape"
print "Exiting..."
