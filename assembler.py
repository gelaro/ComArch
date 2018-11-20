#!/usr/bin/python3
import sys

opcodeDict = {'add': '000',
              'nand': '001',
              'lw': '010',
              'sw': '011',
              'beq': '100',
              'jalr': '101',
              'halt': '110',
              'noop': '111'}

# create memory name label
labels = {}			

# do two complement 
def two_complement(num):
    if (num & (1 << ('{0:016b}'.format(num) - 1))) != 0: # if sign bit is set 
        num = num - (1 << '{0:016b}'.format(num))        # compute negative value
    return num                                           # return positive value as is

# convert binary to decinal 
def binaryList_to_decimal(binaryList):
    out = []
    for line in binaryList:
        try:
            out.append(int(line, 2))
        except TypeError:
            out.append(line)
    return out

#translate register for R-type instruction
def R_type(instruction):
    def R_typeRegisterTranslator(line):
    out = ''
    i = 2
    while i < line.__len__():
        if line[i].isdecimal():
            if (int(line[i]) > 7 or int(line[i]) < 0):
                exit(1)  # detect invalid register error(register)
            if i == line.__len__() - 1:
                out += '0000000000000' + '{0:03b}'.format(int(line[i]))
            else:
                out += '{0:03b}'.format(int(line[i]))
        else:
            exit(1)  # exit if use non number in register field.
        i += 1
    return out
