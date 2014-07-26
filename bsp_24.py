#! /usr/bin/env python

# Diffie-Hellman-Schluesselvereinbarung
# Bsp 24
# g = 2
# p = 101
# m = 14
# n = 27

g = 2
p = 101
m = 14
n = 27

array_all_numbers = []
loop1 = 0
while loop1 < p:
    loop2 = 0
    while loop2 < p:
        #print("r = " + str(n**loop1 % p) + "     s = " + str(m**loop2 % p))
        if (n**loop1 % p) == (m**loop2 % p):
            array_all_numbers.append([loop1, loop2])
            #print("Number a = " + str(loop1))
            #print("Number b = " + str(loop1))
            #break 
        loop2 += 1
    loop1 += 1

print(str(array_all_numbers))
