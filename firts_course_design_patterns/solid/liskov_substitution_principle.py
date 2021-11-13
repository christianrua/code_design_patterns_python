class Rectange:
    def __init__(self, width, height):
        self._height= height
        self._width = width
        
    @property
    def area(self):
        return self._height * self._width

    def __str__(self):
        return f'Width: {self._width}, height: {self._height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height  

    @height.setter
    def height(self, value):
        self._height = value    


class Square(Rectange):
    def __init__(self, size):
        Rectange.__init__(self, size,size)

    @Rectange.width.setter
    def width(self, value):
        self._width = self._height = value   

    @Rectange.height.setter
    def height(self, value):
        self._width = self._height = value     
        

def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'Expectred an area of {expected}, got {rc.area}')    



rc = Rectange(2,3)
use_it(rc)

sq = Square(5)
use_it(sq)

