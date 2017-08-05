#!/usr/bin/python
table = ''
for i in range(32,124,16):
	table+=' '.join(map(chr,range(i,i+16)))+'\n'
while 1:
	print(table)
	i=ord(raw_input())*2-64
	table = table[:i] + ' ' +table[i+1:]	






