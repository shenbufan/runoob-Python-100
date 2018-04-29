# -*- coding:UTF-8 -*-
string = raw_input('please input a string :')
string = string.upper()
file = open('upper.txt','w')
file.write(string)
file.close()