#!/usr/bin/python3
# print State
def printState(reg,pc,lines): 
    memory=[]
    print('\n@@@')
    print('state:')
    print('\tpc'+str(pc))
    print('\tmemory:')
    for i in range(0,len(lines)):
        print("\t\tmemory [" + str(i) + "] = "+str(memory[i]) )  
    print('\tregisters:')
    for j in range(0, 8):
        print("\t\treg[" + str(j) + "] = "+str(reg[j]) ) 
    print('end state')

def simulator (code):
        lines = []
        reg = [0, 0, 0, 0, 0, 0, 0, 0]
        count = 0
        pc = 0
        memory=code.readlines()
        for x in range(len(memory)):
                 print("\t\tmemory [" + str(x) + "] = "+str(memory[x]) )
 
        while 1 :
                count+=1 #total instruction              
                binary=bin(int(memory[pc]))[2:].zfill(32)
                opcode=binary[7:10] #bit 24-22
                A=int(binary[10:13],2)  #bit 21-19
                B=int(binary[13:16],2)  #bit 18-16
                rd=int(binary[29:32],2)    #bit 2-0
                if  binary[16] == "1" :
                    offsetField=int(binary[16:32],2)-(1<<16)
                else :
                    offsetField=int(binary[16:32],2)
 
                if(opcode == "000"): #and
                        reg[rd]=reg[A]+reg[B]  
                        pc+=1                
                elif opcode == "001": #Nand
                        reg[rd]= ~ (reg[A] & reg[B])
                        pc+=1  
                elif opcode == "010": #lw
                        try :
                                reg[B]=int(memory[reg[A]+offsetField])
                                pc+=1
                        except IndexError :
                                print("index ")  
                elif opcode == "011": #sw
                        if(reg[A]+offsetField>len(memory)-1) :
                                memory.append(str(reg[B]))
                        else:                                
                                memory[reg[A]+offsetField]=str(reg[B])
                        pc+=1  
                elif opcode == "100": #beq
                        if reg[A] == reg[B]:
                            pc=pc+offsetField+1
                        else: pc=pc+1
                elif opcode == "101": #jalr
                        if A==B:
                                reg[B]=pc+1
                                pc=pc+1
                        else:
                                reg[B]=pc+1
                                pc=reg[A]
                elif opcode =="110":
                    pc+=1  
                    break
                else : pc+=1                
                printState(reg,pc,lines)
        print("machine halted total of "+str(count)+" instructions executed final state of machine:")
        printState(reg,pc,lines)
simulator(open('Output.out'))