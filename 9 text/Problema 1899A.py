t = int(input())
while t < 1 or t > 100:
    t = int(input())

for _ in range(t):
    n = int(input())
    while n < 1 or n > 1000:
        n = int(input())

    if n % 3 == 0:
        print("Second")
    else:
        print("First")
