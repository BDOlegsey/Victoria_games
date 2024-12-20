s = [[j + i * 4 for j in range(4)] for i in range(4)]

print(s)


for i in range(4):
    for j in range(4):
        print(s[i][j], end=' ')
    print()

print('--------------------------------')

st = set()

a = [1, 7, 3, 8, 3, 4, 4, 5, 2, 5, 5]

st = set(a)

print(len(st))

print(st)

for el in st:
    print(el, end=' ')
print()

st.add(6)

print(st)

if 9 in st:
    print('YES')

print('--------------------')

sl = dict()

sl = {
    'mar': 100,
    'sgfh': 15426,
}

print(sl['mar'])

sl.keys()

for value in sl.values():
    print(value)

if 'mart' in sl:
    print('HEllo')


s = dict(zip('qwerty', list(range(1, 7))))

print(s)
