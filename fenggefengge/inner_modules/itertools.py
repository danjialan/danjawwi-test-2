# import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

import itertools
natuals = itertools.count(1)
dan = itertools.takewhile(lambda x: x <= 5, natuals)
for i in dan:
    print(i)