h = input('請輸入身高：')
w = input('請輸入體重：')
h = int(h)
w = int(w)
x = w/(h*h)*10000 
if x < 18.5:
	print('體重過輕')
elif 18.5 <= x < 24:
	print('正常範圍')
else:
	print('過重')

