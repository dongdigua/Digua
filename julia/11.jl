t1=1
t2=1
print(">")
myn=readline()
n=parse(Int,myn)
for i in 1:n
	global t1,t2
	print(t1,"\t")
	t3=t1+t2
	t1=t2
	t2=t3
end
