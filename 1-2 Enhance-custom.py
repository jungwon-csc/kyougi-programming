initial_name = input()
N = int(input())
i = list(map(int, input().split(' ')))
print(initial_name, end=' ')
for temp in range(N):
    print('a'*i[temp], end='')
    if temp == N-1:
        break
    else:
        print(' ', end='')