print(">")
myn=readline()
n=parse(Int,myn)
coef=1
for i in 0:n
	global coef
	for space in 1:n-i
		print("  ")
	end
	for j in 0:i
		if (j==0 || i==0)
			coef=1
		else
			coef=Int(coef*(i-j+1)/j)
		end
		print("  ",coef," ")
	end
	println()
end

