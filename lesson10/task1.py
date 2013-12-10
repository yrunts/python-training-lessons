"""Solution to task 1 from lesson 10."""


class Color(object):
    """Color representation.

    Attr:
        - code: an `int` color code in hex;
    """
    def __init__(self, code):
        super(Color, self).__init__()
        self.code = code


class Coords(object):
    """Coordinates representation. """
    def __init__(self):
        raise NotImplementedError('Use static methods to get coords instances')

    @staticmethod
    def linear(x, y):
        """Instantiates linear coordinates."""
        return type('Coords', (), {'x': x, 'y': y, 'type': 'linear'})

    @staticmethod
    def cyllindric(p, f, z):
        """Instantiates cyllindric coordinates."""
        return type('Coords', (),
                    {'p': p, 'f': f, 'z': z, 'type': 'cyllindric'})

    @staticmethod
    def radial(r, i, a):
        """Instantiates radial coordinates."""
        return type('Coords', (),
                    {'r': r, 'i': i, 'a': a, 'type': 'radial'})


class Shape(object):
    """Graphical shape base class."""
    pass


class Point(Shape):
    """Point representation.

     Attr:
        - position: a `Coords` point position;
        - color: a `Color` fill color;
    """
    def __init__(self, position, color):
        super(Point, self).__init__()
        self.position = position
        self.color = color


class ColoredShape(Shape):
    """Shape with stroke and fill colors.
    
    Attr:
        - stroke: a `tuple (Color, length)` stroke colors;
        - fill: a `tuple (Color, length)` fill colors;
    """

    def __init__(self, stroke, fill):
        super(ColoredShape, self).__init__()
        self.stroke = stroke
        self.fill = fill


class Line(ColoredShape):
    """Line representation.

    Attr:
        - a: a `Coords` start line position;
        - b: a `Coords` end line position;
    """
    def __init__(self, a, b, stroke):
        super(Line, self).__init__(stroke, None)
        self.a = a
        self.b = b


class Circle(ColoredShape):
    """Circle representation.

    Attr:
        - center: a `Coords` circle center position;
        - radius: a `Number` circle radius length;
    """
    def __init__(self, center, radius, stroke, fill):
        super(Circle, self).__init__(stroke, fill)
        self.center = center
        self.radius = radius


class Rectangle(ColoredShape):
    """Rectangle representation.

    Attr:
        - a: a `Coords` top left point position;
        - b: a `Coords` top right point position;
        - c: a `Coords` bottom right point position;
        - d: a `Coords` bottom left point position;
    """
    def __init__(self, a, b, c, d, stroke, fill):
        super(Rectangle, self).__init__(stroke, fill)
        self.a = a
        self.b = b
        self.c = c
        self.d = d


class Triangle(ColoredShape):
    """Triangle representation. 

    Attr:
        - a: a `Coords` triangle corner position;
        - b: a `Coords` triangle corner position;
        - c: a `Coords` triangle corner position;
    """
    def __init__(self, a, b, c, stroke, fill):
        super(Triangle, self).__init__(stroke, fill)
        self.a = a
        self.b = b
        self.c = c


def main():
    a = Color(111111)
    b = Triangle(1, 2, 3, None, None)
    print b.__doc__


if __name__ == '__main__':
    main()
