n, m = map(int, input().split())
min_package = 1001
min_price = 1001

for _ in range(m):
    a, b = map(int, input().split())
    min_package = min(min_package, a)
    min_price = min(min_price, b)

cost_single = n * min_price

packages = n // 6
remainder = n % 6
cost_mix = (packages * min_package) + (remainder * min_price)
print(min(cost_single, cost_mix))




