
def soma_ate(n):
    if n == 0:
        return 0
    return n + soma_ate(n - 1)

print(soma_ate(10))