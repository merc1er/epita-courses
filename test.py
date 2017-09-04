# Global variables

mod = 0
nb_char = 0
tmp = 0

while True:
	key = input()
	if key == "e":
		if nb_char != 0 and mod == 0:
			print("Door opens")
			mod = 0
			tmp = 0
			nb_char = 0
		else:
			print("Door does not open")
	else:
		nb_char += 1
		tmp = mod * 10 + int(key)
		mod = tmp % 7
