gongnen=input("你好，请问你想要什么功能？")
def fenkai():
    a=input("请输入：")
    b=len(a)
    for i in range(b):
        print(a[i])

def pingfang():
    a=input("请输入：")
    b=len(a)
    d=0
    for i in range(b):
        f=a[i]
        if f % 2==0:
            c=a**a
            e=d+c
    print(e)

if gongnen=="fenkai":
    fenkai()        
elif gongnen=="pingfang":
    pingfang()