#!/usr/bin/python3
""" Square """


from .rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a Square instance """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, v):
        self.width = v
        self.height = v

    def update(self, *args, **kwargs):
        """ Update attributes """
        att = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, att[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
