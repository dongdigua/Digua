print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do;')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans /100
    crates = jars / 100
    return jelly_beans, jars, crates #把数值返回到变量上


start_point = 10000
beans, jars, crates = secret_formula(start_point)


print("With a starting point of: {}".format(start_point)) #把start_point格式化到{}里

print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) #把

print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
#一变成，完美！
#formula：公式
#crate：箱子
#jelly：果冻
