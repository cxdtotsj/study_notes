# Strings

# s = 'a\nb\tc\vd'
# print(s)
# print(len(s))

# s = 'hello'
# s = 'H' + s[1:]
# print(s)
# s = s.replace('h', 'H')
# print(s)

# l = []
# for n in range(0,100000):
#     l.append(str(n))
# l = ''.join(l)
# l = ''.join(map(str, range(0,100000)))
# print(l)


import time
start_time = time.perf_counter()
s = ''
for n in range(0,100000):
    s += str(n)
end_time = time.perf_counter()
print(f'Time elapse: {end_time-start_time}')

start_time = time.perf_counter()
s = []
for n in range(0,100000):
    s.append(str(n))
s = ''.join(s)
end_time = time.perf_counter()
print(f'Time elapse2: {end_time-start_time}')

start_time = time.perf_counter()
s = ''.join(map(str, range(0,100000)))
end_time = time.perf_counter()
print(f'Time elapse3: {end_time-start_time}')
