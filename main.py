class point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return point(x,y)
p1 = point(10,100)
p2 = point(100, 1000)
print(p1 + p2)
