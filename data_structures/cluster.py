from data_structures import network_collection



class Cluster():
    def __init__(self, name,  security_level, networks = None):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """
        if name == "":
            raise ValueError("Name not Gigen")

        self.name = name

        if networks is None:
            self.networks = [network_dict.NetworkCollection(ipv4_network,raw_entry_list)]
        else:
            self.networks = networks

        if security_level == "":
            raise ValueError("The securitry level is not there!")

        self.security_level = security_level

        #super().__init__(self)

        # Setter
        @property
        def name(self):
            return self.__dict__['name']

        @name.setter
        def name(self, value):
            self.__dict__['name'] = ensure_type(value, str)

        @property
        def security_level(self):
            return self.security_level

        @security_level.setter
        def security_level(self, value):
            self.__dict__['security_level'] = ensure_type(value, int)



    def add_networks(self, name, security_level, networks):
        self.networks = self.networks.extend(network_collection.NetworkCollection(ipv4_network, raw_entry_list))
        return self.networks

    def __repr__(self):
        return "Cluster ('{}', '{}', {})".format(self.name, self.security_level, self.networks)

    def __str__(self):
        return "Cluster ('{}', '{}', {})".format(self.address, self.security_level, self.networks)    
