def maior_pontuacao(J):
    N = len(J)
    M = len(J[0])

    dp = [[0] * M for _ in range(N)]

    dp[0][0] = J[0][0]

    for j in range(1, M):
        dp[0][j] = dp[0][j-1] + J[0][j]

    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + J[i][0]

    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = J[i][j] + max(dp[i-1][j], dp[i][j-1])

    return dp[N-1][M-1]


mapa = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

print(maior_pontuacao(mapa))  # 12