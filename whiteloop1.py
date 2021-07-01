#save file as whiteloop1.py

d = 0 # d is the counter
while d < 21:
	squared = d*d
	print(d,squared," ",end="")
	d=d+1
	if(d % 5 == 0):
		print()
