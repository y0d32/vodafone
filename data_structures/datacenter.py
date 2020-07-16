import re

class Datacenter:
    def __init__(self, name, cluster_dict = None):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """
        if name == "":
            raise ValueError("Name not Gigen")

        self.name = name

        if cluster_dict is None:
            self.cluster_dict = {cluster.Cluster(name,security_level,network_dict)}
        else:
            self.cluster_dict = cluster_dict

        # Setter
        @property
        def name(self):
            return self.__dict__['name']

        @name.setter
        def name(self, value):
            self.__dict__['name'] = ensure_type(value, str)




    @staticmethod
    def remove_invalid_clusters(cluster_dict):
        """
        Removes invalid objects from the clusters list.
        """
        pattern = "[A-Z]{3}\-[0-9]{1,3}$"

        for k, v in cluster_dict.items():
            matched = re.match(pattern, k)
            if not matched:
                cluster_dict.pop(k, None)
                #delete object

    def add_child(self, cluster):
        self.cluster_dict.append(cluster)


    def __repr__(self):
        return "DataCenter ('{}', '{}')".format(self.name, self.cluster_dict)

    def __str__(self):
        return "DataCenter ('{}', '{}')".format(self.name, self.cluster_dict)    
