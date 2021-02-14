a=0
while a<10
	global a #while产生新的作用域
	print(a)
	a += 1
end
