def intcode(newprogram):
    program_is_running=1
    i=0
    while program_is_running==1:
        # print('Instruction pointer is : ',i, 'program is : ',newprogram[i])
        if newprogram[i]=='1': # This is Opcode 1 (which means addition)
            address1=int(newprogram[i+1])
            address2=int(newprogram[i+2])
            address3=int(newprogram[i+3])
            result = int(newprogram[address1])+int(newprogram[address2])
            newprogram[address3]=result
            # print('This is an addition: Opcode = ',newprogram[i],'Addition is ',newprogram[address1],' + ', newprogram[address2],'equals ',result,'. Address3 is: ', address3)
            
        elif newprogram[i]=='2': # This is Opcode 2 (which means multiplication)
            address1=int(newprogram[i+1])
            address2=int(newprogram[i+2])
            address3=int(newprogram[i+3])
            result = int(newprogram[address1])*int(newprogram[address2])
            newprogram[address3]=result
            # print('This is a multiplication: Program = ',newprogram[i], 'Multiplication is ',newprogram[address1],' * ', newprogram[address2],'equals ',result, '. Address3 is: ', address3)
            
        elif newprogram[i]=='99':  # This is Opcode 99 (which means terminaison)
            program_is_running=0
            # print('Program terminated')
            return newprogram[0]
        else:
            print('FATAL ERROR: unknown program')
        i+=4
        # print('The new Instruction pointer will be : ',i,'\n\n')