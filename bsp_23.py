#! /usr/bin/env python

text = "FJBFUFXFTTEINVGTUFNVPVIJUUPBEIFFOGTBUOBPUFPCNBKTGEGBXJIOGSGCGOCOPUVOBPTNCMGSYFKTGXKSFEGSVFZUKOOFJSCQNTBXGJVFKMGHGUGJNUWVPEFFTWGSUDJOWCFFTDCFUBTDJJMGHSGNKUJUKMHFGJPFUTEINVGTUFNXQSVFUGGTVHGMGHV"
#text = "HALLO"
file_in = open("caesar_brute_force_2.txt", "w")

alphabet_number = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphabet_letter = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

limit_alphabet = len(alphabet_number)
limit_text = len(text)

loop = 0
while loop < limit_alphabet:
	loop2 = 0
	while loop2 < limit_alphabet:
		is_other_key = False
		loop3 = 0
		file_in.write(str(loop) + "," + str(loop2) + ":\n")
		while loop3 < limit_text:
			if is_other_key == False:
				print(alphabet_number[(alphabet_letter[text[loop3]] + loop) % limit_alphabet]),
				file_in.write(alphabet_number[(alphabet_letter[text[loop3]] + loop) % limit_alphabet])
				is_other_key = True
			else:
				print(alphabet_number[(alphabet_letter[text[loop3]] + loop2) % limit_alphabet]),
				file_in.write(alphabet_number[(alphabet_letter[text[loop3]] + loop2) % limit_alphabet])
				is_other_key = False
			loop3 += 1
		print("\n\n")
		file_in.write("\n\n")
		loop2 += 1
	loop += 1
	print(str(loop) + str(loop2))
print("\n\n")
file_in.close()
