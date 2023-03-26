MAX_N = 100000
sieve = [0] * (MAX_N+1)
for i in range(2, MAX_N+1):
    if sieve[i] == 0:
        for j in range(i, MAX_N+1, i):
            sieve[j] += 1

# read input and process test cases
T = int(input())
for _ in range(T):
    A, B, K = map(int, input().split())
    count = 0
    for i in range(A, B+1):
        if sieve[i] == K:
            count += 1
    print(count)
