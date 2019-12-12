def Count(number,digit):
	time=0
	for i in str(number):
		if i == str(digit):
			time+=1
	return time
a=Count(int(input()),int(input()))
print(a)
