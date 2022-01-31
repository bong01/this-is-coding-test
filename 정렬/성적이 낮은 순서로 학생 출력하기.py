n = int(input())
dic = {}
for i in range(n):
    data = input().split()
    dic[data[0]] = int(data[1])

result = sorted(dic.items(), key=lambda x: x[1])
for k, v in result:
    print(k, end=' ')
