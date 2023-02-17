
class Static:
    def __init__(self):
        self.params = (0.0, 0.0, 0.0)
        self.imagePath = None

    def get_params(self):
        return self.params

    def set_params(self, params):
        self.params = params


class Circle(Static):
    def __init__(self, pos, r):
        super(Circle, self).__init__()
        self.pos = pos
        self.radius = r


class Rectangle(Static):
    def __init__(self, pos, dim):
        super(Rectangle, self).__init__()
        self.pos = pos
        self.dim = dim


class Dynamic:
    def __init__(self, pos, r, params, path):
        self.pos = pos
        self.radius = r
        self.params = params
        self.imagePath = path

    def set_params(self, params):
        self.params = params

    def get_params(self):
        return self.params
