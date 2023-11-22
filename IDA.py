class Tree:
    def __init__(self, value, cost):
        self.root= None
        self.value= value
        self.cost= cost
        self.child= []

    
"""
x= Tree(value=12, cost= 35)
y= Tree(value=20, cost=20)
x.child.append(y)
y.root = x
"""

