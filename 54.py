# -*- coding:UTF-8 -*-
if __name__ == '__main__':
    a = int(raw_input('input a number:\n'))
    b = a >> 4
    b = b & 15
    #c = ~(~0 << 4)
    #d = b & c
    print '%o' %(b)