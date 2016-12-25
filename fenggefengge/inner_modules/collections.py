# from collections import defaultdict
# dd = defaultdict(lambda : 'N/A')
# dd ['1'] = 'a'
# print(dd['1'])
# dd ['2'] = 'b'
# print(dd['2'])
# print(dd['3'])

# from collections import OrderedDict
# d = OrderedDict()
# d['1'] = 'a'
# d['2'] = 'b'
#
# print(d[('1')])
# print(d[('2')])

from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
    print(c[ch])

print(c)