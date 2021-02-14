using Base
using SHA
data=Dict()

function signup()
	print("username>")
	user=readline()
	print("passwd>")
	passwd=readline()
	pass=bytes2hex(sha256(passwd))
	data["$user"]=pass
end

function login()
	print("username>")
	user=readline()
	print("passwd>")
	passwd=readline()
	pass=data["$user"]
	mypass=bytes2hex(sha256(passwd))
	if mypass==pass
		println("login succeed")
	else
		println("login failed")
	end
end

while 1==1
print("signup(0) or login(1)?")
print(">")
n=parse(Int,readline())
local n
if n == 0
	signup()
elseif n == 1
	login()
elseif n == 99
	println(data)
else
	print("error")
end
end

#=
signup()
println(data)
login()
=#



