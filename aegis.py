from itertools import count

class Aegis:
    """
        Base class for all Aegis objects

        ...

        Attributes
        ----------
        about : str
            a formatted string to print out the store properties
        name : str
            the name of the object
        description : str
            what does this object represent?

        Methods
        -------
        getInstanceCount : int
            return the number of objects of this class created
        """

    _ids = count(0)

    def __init__(self):
        """
        Parameters
        ----------
        name : str, optional
            the name of the store
        description : str
            what does this object represent?
        """

        self.name = "Aegis"
        self.id = next(self._ids)
        self.description = "A basic object."

    def getInstanceCount(self):
        """
        Get the bucket_count of objects created by this class
        :return:
        """
        return self._ids



