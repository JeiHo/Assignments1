import sys
x = float(sys.argv[1])

def grade():
	if x>=0 and x<1:
		print("F")
	elif x<1.5:
		print("D-")
	elif x<2:
		print("D")
	elif x<2.5:
		print("D+")
	elif x<2.85:
		print("C-")
	elif x<3.2:
		print("C")
	elif x<3.5:
		print("C+")
	elif x<3.85:
		print("B-")
	elif x<4.2:
		print("B")
	elif x<4.5:
		print("B+")
	elif x<4.65:
		print("A-")
	elif x<4.85:
		print("A")
	elif x<5:
		print("A+")
	else:
		print("Please input number between 0 to 5")
grade();

