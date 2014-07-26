#! /usr/bin/env python

text = "TYUIUH JUNJ MKHTU CYJ UYDUH SQUIQHSXYVVHU CYJ UYDUC LUHISXKR LED IUSXPUXD LUHISXBKUIIUBJ. TYUIU QHJ TUH LUHISXBKUIIUBKDW DUDDJ IYSX QKSX HEJ D KDT AQDD IUXH BUYSXJ YC YDJUHDUJ UDJISXBKUIIUBJ MUHTUD"

alphabet_number = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphabet_letter = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

limit_alphabet = len(alphabet_number)
limit_text = len(text)

loop = 0
while loop < limit_alphabet:
	loop2 = 0
	while loop2 < limit_text:
		if text[loop2] != ' ' and text[loop2] != '.':
			print(alphabet_number[(alphabet_letter[text[loop2]] + loop) % limit_alphabet]),
		else:
			if text[loop2] == '.':
				print(text[loop2]),
			else:
				print(text[loop2])
		loop2 += 1
	print("\n\n")
	loop += 1
