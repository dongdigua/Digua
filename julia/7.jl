print("heshu>")
myn=readline()
n=parse(Int,myn) #转化
print("n is: $n =")

#x=ceil(sqrt(n))


for i in 2:n
	global n
	local i #将i引入到whlie循环中
	while n % i == 0
		print(i)
		n=n/i
		if n!=1
			print("*")
		end
	end
end

#之后试着并行处理一下
