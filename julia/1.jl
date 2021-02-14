"""
    walk(T) -> trajectory
suijixingzou
"""
function walk(T)
	x=0
	trajectory = [x] 

	for t in l:T
		if rand() < 0.5
			x += 1
		else
			x -= 1
		end
		push!(trajectory, x)
	end
	return trajectory
end



