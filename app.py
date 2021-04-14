#!/usr/bin/env Python3

from os import system

system( "clear" )

file = open( "in.txt", "r" )

fileContent = file.read()

listContent = fileContent.split()

a = int( listContent[0] )
b = int( listContent[1] )
r = a + b

print( f"Result = {r}" )

