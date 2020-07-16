#from data_structures import network_collection
from datetime import date


class Entry():
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """
        if address == "":
            raise ValueError("The address was not given")

        self.address = address


        if available == "":
            raise ValueError("We don't know if is available or not")

        self.available = available


        self.last_used = last_used
        #super().__init__(self)

        # Setter
        @property
        def address(self):
            return self.__dict__['address']

        @address.setter
        def address(self, value):
            self.__dict__['address'] = ensure_type(value, str)

        @property
        def available(self):
            return self.available

        @available.setter
        def available(self, value):
            self.__dict__['available'] = ensure_type(value, bool)


        @property
        def last_used(self):
            return self.last_used

        @last_used.setter
        def last_used(self, value):
            self.__dict__['last_used'] = ensure_type(value, date)
            

    def __repr__(self):
        return "Entry ('{}', '{}', {})".format(self.address, self.available, self.last_used)

    def __str__(self):
        return "Entry ('{}', '{}', {})".format(self.address, self.available, self.last_used)
