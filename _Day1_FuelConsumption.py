### Advent of Code 2019
### Day 1


# IMPORTS
import math

# EQUATION
# Fuel = Module_mass / 3 , round down and substract 2

#VARIABLES
Total_Fuel=0

#Get the Module Mass list
rawlist = open('./ressources/Day1_Module_mass.txt','r')
Module_mass = rawlist.readlines()
rawlist.close()

for i in range(len(Module_mass)):
    Total_Module_Fuel=0
    Fuel = math.floor(int(Module_mass[i])/3)-2
    Total_Module_Fuel+=Fuel
    Additional_Fuel = math.floor(int(Total_Module_Fuel)/3)-2
    while Additional_Fuel>0:
        Total_Module_Fuel+=Additional_Fuel
        print('Additional Fuel required is: ',Additional_Fuel)
        print('Total fuel needed is now ',Total_Module_Fuel)
        Additional_Fuel = math.floor(int(Additional_Fuel)/3)-2
    
    print('For a Module mass of ',int(Module_mass[i]),'units, the fuel needed is now ',Total_Module_Fuel,'with the additional fuel')
    Total_Fuel+=Total_Module_Fuel

print('Total fuel needed for the Modules is now ',Total_Fuel)