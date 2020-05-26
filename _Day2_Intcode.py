### Day 2 - Intcode / Opcode

from intcode import intcode
#INIT
program_is_running=1
i=0
noun = 0
verb = 0

# Open file
input = open('Day2_input.txt','r')
program = input.read().split(',')
input.close()
newprogram=program

#Correction of the input file
newprogram[1]=12
newprogram[2]=2

output=intcode(newprogram) #Runs the tape through the program

print('The output of the program is: ', output)