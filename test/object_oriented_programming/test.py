class WaLun(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('name:%s score:%s' %(self.name,self.score))

dan=WaLun('Danjawwi',60)
yu=WaLun('YuSang',60)

dan.print_score()
yu.print_score()