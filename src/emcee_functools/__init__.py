class Fixed(object):
    '''
    Class describing a parameter which does not vary
    '''

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, *args, **kwargs):
        raise ValueError("Fixed values cannot change")

    def __add__(self, other):
        raise ValueError("Fixed values cannot change")

    def __str__(self):
        return '<Fixed value {value}>'.format(value=self.value)


class Varying(object):
    '''
    Placeholder for varying parameter
    '''
