# 列表中使用 lambda
print([(lambda x: x*x)(x) for x in range(10)])

print('-------------------------------------')

l = [(1, 20), (3, 0), (9, 10), (2, -1)]
print((lambda x: x[1]) for x in l)
