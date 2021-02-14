def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
# 上面是函数
#下面是函数的几种运行/调用/使用函数的方法
print("We can just give the function nembers directly:")
cheese_and_crackers(20,30) #不必须有空格


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)