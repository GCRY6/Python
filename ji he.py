gongnen=input("你好，请问你想要什么功能？")
def fenkai():
    a=input("请输入：")
    b=len(a)
    for i in range(b):
        print(a[i])

def pingfang():
    a=input("请输入：")
    a=a.split()
    a=[int(num) for num in a]
    d=0
    for i in range(len(a)):
        f=a[i]
        if f % 2==0:
            c=f*f
            d+=c
    print(d)

if gongnen=="fenkai":
    fenkai()        
elif gongnen=="pingfang":
    pingfang()