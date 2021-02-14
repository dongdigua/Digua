#这个代码用来加密单词
a=str(input('word:'))
b=int(input('number:'))
alphabet="abcdefghijklmnopqrstuvwxyz"
word=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for x in a:
    c=int(word.index(x))               #从字母表中找到单词的索引(对应数字)
    d=c+b                
    print(alphabet[d],end='')          #输出加密后单词(不换行输出)
print(' ''key:',b)