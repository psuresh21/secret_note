import datetime
import random
print("---------------------------------------------------------")
mydt = datetime.datetime.now()
print("welcome to secret Note")
print("it will store the information with password \n and restore your password")
print("Copyright (c) " + mydt.strftime("%Y") + " Suresh Pandiyan \n")

listy = ['store your info','retreive your info','exit']

option = 1
running = True

while(running):
	option = 1
	for num in listy:
		print(str(option) + "." + num)
		option = option + 1
	yx = int(input("enter your number: "))

	if yx == 1:
		first_pass = str(input("enter your password: "))
		refirst_pass = str(input("re-enter your password: "))
		store = []
		passwd = []

		if first_pass == refirst_pass:
			x = str(input("store some information "))
			passwd.append(first_pass)
			store.append(x)
		else:
			print("failed")
			#first_pass = str(input("enter your password: "))
			#refirst_pass = str(input("re-enter your password: "))
			
		with open("pass436790.txt","a") as passd:
			print("%s %s" % (first_pass,x), file=passd)	
	if yx == 2:
		y = str(input("enter your password for show information "))
		passy = []
		#infos = []
		with open("pass436790.txt","r") as passd:
			for k in passd:
				(passd,infod) = k.split(' ',1)
				m = {}
				m['pass'] = passd
				m['info'] = infod
				#print(m['pass'])
				if m['pass'] == y:
					print(m['info'])
				else:
					while 0 < 100:
						k = random.randint(10000000000,60000000000) * 1065456646516591911119198191198191919819199494976549849841984498498343549498481415316118180 * 1065456646516591911119198191198191919819199494976549849841984498498343549498481415316118180
						print(k)
	if yx == 3:
		running = False
