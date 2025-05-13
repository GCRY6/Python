n = input("请输入斐波那契数列的项数：")
fib = []
a, b = 0, 1
for i in range(int(n)):
    fib.append(a)
    a, b = b, a + b
print(f"斐波那契数列的前{n}项是：{fib}")

prime_fib = []
for i in fib:
    if i < 2:
        continue
    is_prime = True
    for num in range(2, int(i**0.5) + 1):
        if i % num == 0:
            is_prime = False
            break
    if is_prime:
        prime_fib.append(i)
print(f"其中的素数是：{prime_fib}")