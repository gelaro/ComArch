#!/user/bin/python3
import sys

opcodeList = {'add': '000',
              'nand': '001',
              'lw': '010',
              'sw': '011',
              'beq': '100',
              'jalr': '101',
              'halt': '110',
              'noop': '111'}

labels = {}			

def two_complement(num):
    if (num & (1 << ('{0:016b}'.format(num) - 1))) != 0: # if sign bit is set 
        num = num - (1 << '{0:016b}'.format(num))        # compute negative value
    return num                         # return positive value as is

