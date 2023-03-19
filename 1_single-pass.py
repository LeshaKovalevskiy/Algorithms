n = int(input())
# 1 Подсчет кол-ва, суммы, произведения
cnt = 0
s = 0
p = 1
for i in range(n):
    num = int(input())
    if num > 10:
        cnt += 1
        s += num
        p *= num
print(cnt, s, p, sep='\n')

# 2. Поиск минимум(максимум)
smallest = int(input())
for i in range(n - 1):
    num = int(input())
    if smallest > num:
        smallest = num
print(smallest)

# 3. Сигнальные метки(определение простое ли число)
flag = True
num = int(input())

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
print("YES" if flag else "NO")
