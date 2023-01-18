def love_numbers(x):
    size = len(x)
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j]:
                x[i] = ""
                x[j] = ""
    x = [i for i in x if i != ""]
    return x

listarr = []
while True:
    n = int(input())
    if n == 0:
        break
    arr = list(map(int, input().split()))
    listarr.append(love_numbers(arr))

for i in listarr:
    print(*i)