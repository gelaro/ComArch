#!/usr/bin/python3
#coding: utf-8 
listCommand = ['add','nand','lw','sw','beq','jalr','halt','noop']

def def_type(i) :
    if i[0] in listCommand or i[1] in listCommand :
        #o type
        if i[0]=='halt' or i[0]=='noop' :     
            return O_type(i,0)
        elif i[1]=='halt' or i[1]=='noop' :
            return O_type(i,1) 

        #r type
        elif i[0]=='add' or i[0]=='nand' :  
            return R_type(i, 0)
        elif i[1]=='add' or i[1]=='nand' :
            return R_type(i,1)

        #i type 
        elif i[0] =='lw' or i[0]=='sw' or i[0]=='beq' :  
           return I_type(i,0)
        elif i[1] =='lw' or i[1]=='sw'or i[1]=='beq':
           return I_type(i,1)

        #j type
        elif i[0] =='jalr' : 
            return J_type(i,0)
        elif i[1] =='jalr' :
            return J_type(i,1)   
        
    elif i[1]=='.fill':
        return i[2]
    
    else :
        print('wrong opcode')
        exit(1)

def R_type(i, index_command) :
    # print(i)
    if i[index_command] == "add":
        command = "000"
    elif i[index_command] == "nand":
        command = "001"

    rs = '{0:03b}'.format(int(i[index_command+3])) 
    rt = '{0:03b}'.format(int(i[index_command+2]))
    rd = '{0:03b}'.format(int(i[index_command+1]))
        
    binaryNum = str(command + rs + rt + "0000000000000" + rd)
    return binaryNum
        
def I_type(i, index_command) :
    if i[index_command] == "lw":
        command = "010"
    elif i[index_command] == "sw":
        command = "011"
    else :
        command = "100"
        
    rs = '{0:03b}'.format(int(i[index_command+1])) 
    rt = '{0:03b}'.format(int(i[index_command+2]))
    offset = '{0:016b}'.format(int(i[index_command+3]))
    if len(offset) > 16 :           #offset ไม่เกิน 16
        print('offset more than 16')
        exit(1)
        
    if(offset[0]=='-'):
       offset = offset.replace('0','-')
       offset = offset.replace('1','0')
       offset = offset.replace('-','1')
            
    #print(command, rs, rt, offset)
    binaryNum = str(command + rs + rt + offset)
    #print(binaryNum)
    #print(int(binaryNum, 2))
    return binaryNum

def J_type(i,index_command):
    command = "101"
        
    rs = '{0:03b}'.format(int(i[index_command+2])) 
    rd = '{0:03b}'.format(int(i[index_command+1]))
        
    binaryNum = str(command + rs + rd + "0000000000000000")
    #print(binaryNum)
    #print(int(binaryNum, 2))
    return binaryNum

def O_type(i,index_command):
    
    if i[index_command] == "halt" :
        command = "110"
    elif i[index_command] == "noop" :
        command = "111" 
        
    binaryNum = str(command + "0000000000000000000000")
        
    return binaryNum
   
if __name__ == "__main__" :
    register_bit = 8 
    computer_bit = 32 
    #word_address = 65536 ;
    
    word_bit = 65536*16
    wb = word_bit 
   # print(wb)
    
    f = open('test_assembly.txt')
    line = f.readlines()
    f.close()
    lineCommand = []
    for i in range(len(line)) :
        lineCommand.append([])
    count = 0
    
    label = []
    
    for i in line :
        tmp = i.split()
        last = -2 if len(tmp[-1])>6 else -1
        
        if(tmp[0] not in listCommand) :     #เช็ค label ซ้ำ
            if(tmp[0] not in label):
                label.append(tmp[0])
            else :
                print('dupilicate label')
                exit(1)
        
        if (not tmp[last].replace('-','0').isnumeric()) and tmp[last] not in listCommand :  #เปลี่ยน label เป็นตัวเลข
            change = 0
            for i in range( len(line) ) :
                if( line[i].find(tmp[last]) == 0 ) :
                    tmp[last] = str(i)
                    if( i < count and tmp[1] != '.fill') :
                        tmp[last] = str(i-count)
                    change = 1
                        
            if(not change):
                print("label undefine")
        
        lineCommand[count].extend(tmp)
        count = count+1
    
    for i in lineCommand :
       try: print(def_type(i))
       except Exception as e:
           exit(1)