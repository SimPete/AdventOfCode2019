### Day 2 - Intcode / Opcode
# PART 2: Change the values at position 1 and 2 to obtain the result 19690720 at position 0. Need to restore the memory between each attempt.  
from intcode import intcode

def main(DESIRED_OUTPUT):
    for noun in range(0,100): 
        for verb in range (0,100):
            #RESET THE MEMORY, RESTART THE PROGRAM
            input = open('Day2_input.txt','r')
            program = input.read().split(',')
            input.close()
            newprogram=program
            
            #Adjust noun and verb
            newprogram[1]=noun
            newprogram[2]=verb

            # print('At START of the loop NEWPROGRAM WAS, output is ',newprogram[0], 'noun is ', newprogram[1],'verb is ',newprogram[2])
            output=intcode(newprogram)        
            # print('At END of the loop NEWPROGRAM WAS, output is ',newprogram[0], 'noun is ', newprogram[1],'verb is ',newprogram[2],'\n')        
            if output == DESIRED_OUTPUT:
                print('EUREKA!!! The answer to the riddle is 100 * noun + verb, which is 100 * ', noun,' + ', verb,' = ', (100*int(noun))+int(verb),'The output is : ',newprogram[0],' which is equal to ',DESIRED_OUTPUT)
                return

DESIRED_OUTPUT=19690720
main(DESIRED_OUTPUT)
