import collections

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# defaultdict
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
# Use dict and setdefault
g = {}
for k, v in s:
    g.setdefault(k, []).append(v)

# Use dict
e = {}
for k, v in s:
    e[k] = v
    ##list(d.items())
    ##list(g.items())
    ##list(e.items())

'''
list(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
>>> list(g.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
>>> list(e.items())
[('blue', 4), ('red', 1), ('yellow', 3)]
>>> d
defaultdict(<class 'list'>, {'blue': [2, 4], 'red': [1], 'yellow': [1, 3]})
>>> g
{'blue': [2, 4], 'red': [1], 'yellow': [1, 3]}
>>> e
{'blue': 4, 'red': 1, 'yellow': 3}
>>> d.items()
dict_items([('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])])
>>> d["blue"]
[2, 4]
>>> d.keys()
dict_keys(['blue', 'red', 'yellow'])
>>> d.default_factory
<class 'list'>
>>> d.values()
dict_values([[2, 4], [1], [1, 3]])
'''