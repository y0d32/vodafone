from data_structures import entry


class NetworkCollection():
    def __init__(self, ipv4_network, raw_entry_list = None):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """
        if ipv4_network == "":
            raise ValueError("Please insert an IPv4")

        self.ipv4_network = ipv4_network


        if raw_entry_list is None:
            self.raw_entry_list = [entry.Entry(address,available,last_used)]
        else:
            self.raw_entry_list = raw_entry_list

        #super().__init__(self)

        # Setter
        @property
        def ipv4_network(self):
            return self.__dict__['ipv4_network']

        @ipv4_network.setter
        def ipv4_network(self, value):
            self.__dict__['ipv4_network'] = ensure_type(value, str)



    @staticmethod
    def remove_invalid_records(ipv4_network,raw_entry_list):
        """
        Removes invalid objects from the entries list.
        """

        for item in raw_entry_list:
            #this will get 192.168.100 from 192.168.100.7
            #Takes from back till . This is my solution to check if substring is in string
            a = item[1].rsplit('.', 1)[0]
            if  a not in ipv4_network:
                raw_entry_list.remove(item)
                #delete object


    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.raw_entry_list = sorted(entry.Entry, key = lambda x: int(x[0]))
        return self.raw_entry_list

    def add_entry_records(self, ipv4_network, raw_entry_list):
        self.raw_entry_list = self.raw_entry_list.extend(entry.Entry(address, available, last_used))
        return self.raw_entry_list

    def __repr__(self):
        return "NetworkCollection ('{}', '{}')".format(self.ipv4_network, self.raw_entry_list)

    def __str__(self):
        return "NetworkCollection ('{}', '{}')".format(self.address, self.security_level)
