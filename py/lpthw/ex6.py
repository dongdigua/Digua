types_of_people = 10
x = f"There are {types_of_people} types of peoele." # f-string

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # f-string

print(x)
print(y)

print(f"I said: {x}") #
print(f"I raid: '{y}'") # ""里的''

hilarious = False # 滑稽
joke_evaluation = "Isn't that joke so funny? {}!" #结尾什么意思?

print(joke_evaluation.format(hilarious)) #为什么是() 啊哈!明白了,格式化的是{}里的内容!!!

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

