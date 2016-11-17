def person(name,age=23,**kw):
    print('name:',name,'age:',age,'qita:',kw)

room={'school':'bjtu','hobby':'dota'}

person('dan',**room)
person('yi',**room)
person('xinjian',**room)