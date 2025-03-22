def fenkai():
    a = input("请输入：")
    for char in a:
        print(char)

def pingfang():
    a = [int(num) for num in input("请输入：").split()]
    d = sum(num * num for num in a if num % 2 == 0)
    print(d)

def ziuzhi():
    a = [int(num) for num in input("请输入：").split()]
    print(f"{max(a)} {min(a)}")

functions = {
    "fenkai": fenkai,
    "pingfang": pingfang,
    "ziuzhi": ziuzhi
}

gongnen = input("你好，请问你想要什么功能？")
function = functions.get(gongnen)
if function:
    function()
else:
    print("输入错误")
