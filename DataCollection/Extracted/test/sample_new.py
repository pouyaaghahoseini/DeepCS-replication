from collections import defaultdict


def square(n):
    '''Takes in a number n, returns the square of n'''
    s = n**2
    return s
def add_binary(a, b):
    '''
    Returns the sum of two decimal numbers in binary digits.

            Parameters:
                    a (int): A decimal integer
                    b (int): Another decimal integer

            Returns:
                    binary_sum (str): Binary string of the sum of a and b
    '''
    c = a + b
    return c

class Person:
    """
    A class to represent a person.

    ...

    Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """

    def __init__(self, name, surname, age):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            name : str
                first name of the person
            surname : str
                family name of the person
            age : int
                age of the person
        """

        self.name = name
        self.surname = surname
        self.age = age

    def info(self, additional=""):
        """
        Prints the person's name and age.

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        None
        """
        info = "this is information"
        print(info)
        print("Name:", self.name)
        print("Surame:", self.surname)
        print("Age:", self.age)

class Person2:
    """
    A class to represent a person.

    ...

    Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """

    def __init__(self, name, surname, age):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            name : str
                first name of the person
            surname : str
                family name of the person
            age : int
                age of the person
        """

        self.name2 = name
        self.surname2 = surname
        self.age2 = age

    def random(self, additional=""):
        """
        Prints the person's name and age.

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        None
        """
        info = "this is random information"
        print(info)
        print("Name:", self.name2)
        print("Surame:", self.surname2)
        print("Age:", self.age2)
    def test(self, additional=""):
        info = "this is random information"
        print(info)
        print("Name:", self.name2)
        print("Surame:", self.surname2)
        print("Age:", self.age2)

class Data(object):
    """Object representing one full stack test."""

    def __init__(self, filename):
        self.title = ""
        self.length = 0
        self.samples = defaultdict(list)

        self._ReadSamples(filename)

    def _ReadSamples(self, filename):
        """Reads graph data from the given file."""
        f = open(filename)
        it = iter(f)

        self.title = it.next().strip()
        self.length = int(it.next())
        field_names = [name.strip() for name in it.next().split()]
        field_ids = [NAME_TO_ID[name] for name in field_names]

        for field_id in field_ids:
            self.samples[field_id] = [0.0] * self.length

        for sample_id in xrange(self.length):
            for col, value in enumerate(it.next().split()):
                self.samples[field_ids[col]][sample_id] = float(value)

        self._SubtractFirstInputTime()
        self._GenerateAdditionalData()

        f.close()

