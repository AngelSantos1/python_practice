class Classist(object):
    def __init__(self):
        self.items = []
    
    def thisClassist(self):
        classScore = 0
        for status in self.items:
            if item == 'car':
                classScore += 2
            elif item == 'job':
                classScore += 4
            elif item == 'house':
                classScore += 6
        return classScore
    
    def addItem(self,item):
        self.items.append(item)
        
me = Classist()

print(me.thisClassist())