from urllib import urlopen
import urllib
a = 0

def startup():
	global a

	while True:
		if a == 0:
			x = raw_input("Welcome to Python isup. Select your command here:\n> ")
			a = 1
		else:
			x = raw_input("> ")

		if x == "help":
			pass

		elif x == "isup":
			z = raw_input("url here:\n> ")
			raw_input(geturl(z))

def geturl(url):
	y = urlopen(url).getcode()
	
	if y == 200:
		print ("%r is up!") % (url)
		startup()
	else:
		print ("%r looks down from here!") % (url)
		startup()

startup()






#Original
# while not False:
# 	if a == 0:
# 		x = raw_input("Welcome to Python isup. Select your command here:\n> ")
# 		a = 1
# 	else:
# 		x = raw_input("")
	
# 	if x == "help":
# 		print ("Available commands:\n isup \n http://")
# 		pass

# 	elif x == "isup":
# 		print ("Type in the adress here")
# 		y = raw_input("> ")
# 		z = urlopen(y).getcode()
# 		if z == 200:
# 			print("The website is up.")
# 			raw_input("")
# 		else:
# 			print ("Your website is down")
# 			raw_input("")
# 	else:
# 		print ("Does not understand. Try again")
# else:
# 	print ("Fatal Error")
# 	exit()