MAX_N = 100000
sieve = [0] * (MAX_N+1)
primes = [[] for _ in range(MAX_N+1)]
for i in range(2, MAX_N+1):
    if sieve[i] == 0:
        for j in range(i, MAX_N+1, i):
            sieve[j] += 1
            primes[j].append(i)

dp = [[0] * (MAX_N+1) for _ in range(6)]
for k in range(1, 6):
    for n in range(2, MAX_N+1):
        if sieve[n] == k:
            dp[k][n] = dp[k][n-1] + 1
        else:
            dp[k][n] = dp[k][n-1]

# read input and process test cases
T = int(input())
for _ in range(T):
    A, B, K = map(int, input().split())
    count = dp[K][B] - dp[K][A-1]
    print(count)
