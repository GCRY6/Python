def split_chars():
    user_input = input("请输入要拆分的字符串：")
    for char in user_input:
        print(char)

def sum_even_squares():
    numbers = [int(num) for num in input("请输入数字，用空格分隔：").split()]
    result = sum(num * num for num in numbers if num % 2 == 0)
    print(f"偶数的平方和是: {result}")

def find_min_max():
    numbers = [int(num) for num in input("请输入数字，用空格分隔：").split()]
    print(f"最大值: {max(numbers)}, 最小值: {min(numbers)}")

functions = {
    "split": split_chars,
    "square": sum_even_squares,
    "minmax": find_min_max
}

print("可用功能: split(拆分字符), square(偶数平方和), minmax(找最大最小值)")
choice = input("请选择功能：").lower()
selected_function = functions.get(choice)
if selected_function:
    selected_function()
else:
    print("错误: 无效的功能选择")