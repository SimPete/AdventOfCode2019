### Advent of Code 2019
### Day 4

# 6-digits number [ALWAYS TRUE WITH THE GIVEN RANGE, NOT CHECKED]
# Between 271973 and 785961 [DONE]
# Two adjacent digits (like 22 in 122345)
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

# How many different passwords within the range given in your puzzle input meet these criteria?

### input = 271973-785961

import re

PART1_valid_iteration = 0
PART2_valid_iteration = 0
valid_condition1 = False
valid_condition_1and2 = False

# starting from 271973 and getting to 785961, we want to check all the numbers to ensure they respect the conditions. If they do, we count them. 

for i in range (271973,785961):
    i_string = str(i)
    valid_condition1 = False
    valid_condition_1and2 = False
    
    # Check condition 1: Adjacent digits
    if i_string[0] == i_string[1]:
        valid_condition1 = True, #print(valid_condition1) #print(i_string)# print("valid condition 1!")
    elif i_string[1] == i_string[2]:
        valid_condition1 = True, #print(valid_condition1) #print(i_string)# print("valid condition 1!")
    elif i_string[2] == i_string[3]:
        valid_condition1 = True, #print(valid_condition1) #print(i_string)# print("valid condition 1!")
    elif i_string[3] == i_string[4]:
        valid_condition1 = True, #print(valid_condition1) #print(i_string)# print("valid condition 1!")
    elif i_string[4] == i_string[5]:
        valid_condition1 = True, #print(bool(valid_condition1)) #print(i_string)# print("valid condition 1!")
    else: 
        valid_condition1 = False
    
    # Check condition 2: Never decreases
    if bool(valid_condition1) == True:
        # print('Valid first condition, checking second condition')
        if i_string[0] > i_string[1]: pass #print('invalid condition 2') 
        elif i_string[1] > i_string[2]: pass #print('invalid condition 2') 
        elif i_string[2] > i_string[3]: pass #print('invalid condition 2') 
        elif i_string[3] > i_string[4]: pass #print('invalid condition 2') 
        elif i_string[4] > i_string[5]: pass #print('invalid condition 2')
        else: 
            PART1_valid_iteration = PART1_valid_iteration + 1
            valid_condition_1and2 = True
            # print("Valid conditions 1&2!", i_string, ", nb of valid iteration is now: ", PART1_valid_iteration)
    
    # Check condition 3: Minimum 1x two digits couple. 
    if bool(valid_condition_1and2) == True:
        # Use the lookahead function to check what is coming after the digit-couple in the i_string. 11 isolated will give len(ans)=1, 111 will give (len(ans)=2 since those are two 11 interlaced. 

            if len([m.start() for m in re.finditer('(?=11)', i_string)])==1 or len([m.start() for m in re.finditer('(?=22)', i_string)])==1 or len([m.start() for m in re.finditer('(?=33)', i_string)])==1 or len([m.start() for m in re.finditer('(?=44)', i_string)])==1 or len([m.start() for m in re.finditer('(?=55)', i_string)])==1 or len([m.start() for m in re.finditer('(?=66)', i_string)])==1 or len([m.start() for m in re.finditer('(?=77)', i_string)])==1 or len([m.start() for m in re.finditer('(?=88)', i_string)])==1 or len([m.start() for m in re.finditer('(?=99)', i_string)])==1:
                PART2_valid_iteration= PART2_valid_iteration + 1 
                print("Valid conditions 1&2&3!", i_string, ", nb of valid iteration is now: ", PART2_valid_iteration)
        
        
print("Total number of valid iteration in PART1: ",PART1_valid_iteration)
print("Total number of valid iteration in PART2: ",PART2_valid_iteration)