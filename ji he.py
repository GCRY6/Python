def fenkai():
    # 获取用户输入的字符串
    a = input("请输入：")
    # 遍历字符串中的每个字符
    for char in a:
        # 打印当前字符
        print(char)

def pingfang():
    # 获取用户输入的字符串，并按空格分割成列表
    a = [int(num) for num in input("请输入：").split()]
    # 计算列表中所有偶数的平方和
    d = sum(num * num for num in a if num % 2 == 0)
    # 打印结果
    print(d)

def ziuzhi():
    # 获取用户输入的字符串，并按空格分割成列表
    a = [int(num) for num in input("请输入：").split()]
    # 打印列表中的最大值和最小值
    print(f"{max(a)} {min(a)}")

# 定义一个字典，将功能名称映射到对应的函数
functions = {
    "fenkai": fenkai,
    "pingfang": pingfang,
    "ziuzhi": ziuzhi
}

# 获取用户输入的功能名称
gongnen = input("你好，请问你想要什么功能？")
# 根据用户输入的功能名称获取对应的函数
function = functions.get(gongnen)
# 如果找到了对应的函数，则调用该函数
if function:
    function()
# 如果没有找到对应的函数，则打印错误信息
else:
    print("输入错误")
