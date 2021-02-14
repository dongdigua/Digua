max = 0
num = 1
while num <= 10
	x=Int(floor(rand()*100))
	println("di $num gesuijishushi $x")
	global num += 1
	global max
	if (x>max) #可以有括号
		max=x 
	end
end
println(max)

