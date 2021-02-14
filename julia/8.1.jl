using Base.Threads

zhishu=[]
zongshu=1000
print("initalizing...")

@threads for n in 2:zongshu
	a=0
	local a
	@threads for i in 2:n-1

		if n%i==0
			
			a=1
		end
	end
	if a==0
		push!(zhishu,n)
		#print("$n is zhishu")
	end
end

println(zhishu)

#================================
================================#
print("[heshu]>")
heshu=readline()
m=parse(Int,heshu)
w=convert(Int,ceil(sqrt(m)))
houmian=[x for x in 1001:w]
g=w
shuzu=zhishu*houmian

yinshu=[]

@threads for s in shuzu
	global w
	local s
	while w%s==0
		print(s)
		push!(yinshu,s)
		w=w/s
		print("*")
	end
end
@threads for u in yinshu
	global g
	g=g/u
end

print(convert(Int,g))
	


