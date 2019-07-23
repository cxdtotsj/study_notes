def createCounter():
    i = 0
    count1 = []
    def counter():
        nonlocal i
        i += 1
        return i
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('success')
else:
    print('fall1')

