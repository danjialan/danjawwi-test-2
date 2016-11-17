def yang(l):
    n=1
    while n<=l:
        g=1
        while g<=n:
            i=1
            j=1
            gt = 1
            nt = 1
            while i <= g:
                gt=gt*i
                i=i+1
            while j <= n:
                nt=nt*1
                j=j+1
            d = gt / nt
            print (d)
            print('-----', n,g)
            g = g+1

        n=n+1

l = int(input('input l'))
yang(l)


