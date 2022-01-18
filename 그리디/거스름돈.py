n = int(input())

coin_type = [500, 100, 50, 10]
c = 0

for coin in coin_type:
    c += n / coin
    n = n % coin

print(c)
