using Base.Threads
print("string>")
str=readline()
print("key>")
key=parse(Int,readline())
alp="abcdefghijklmnopqrstuvwxyz"
result=[]
if key>26
	key=key-26
end

@threads for i in 1:length(str)
	@threads for j in 1:26
		if str[i] == alp[j]
			push!(result,alp[j+key])
		end
	end
end

for k in result
	print(k)
end
