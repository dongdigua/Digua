using Base.Threads

print("[heshu]>")
n=readline()
x=parse(Int,n)
y=ceil(sqrt(x))
z=convert(Int,y)

w=x
a=[]

@threads for i in 2:z
	global x
	local i
	
	while x%i==0
		print(i)
		push!(a,i)
		x=x/i
		print("*")
				
	end
end

@threads for j in a
	global w
	w=w/j
end

print(convert(Int,w))


