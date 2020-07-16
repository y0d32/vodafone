
import unittest
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from  data_structures import network_collection


class TestCluster(unittest.TestCase):

    def testInsufficientArgs(self):
        ipv4_network=""
        raw_entry_list = []

        #self.failUnlessRaises(ValueError, cluster.Cluster, name, security_level, network_dict)
        self.assertRaises(ValueError,network_collection.NetworkCollection, ipv4_network, raw_entry_list)

    def test_initial_value(self):
        obj_1 = network_collection.NetworkCollection(ipv4_network="109.156.104.30",
        raw_entry_list = [1,"Here we go", 2,"Again"])
        assert obj_1.ipv4_network == "109.156.104.30"
        assert obj_1.raw_entry_list == [1,"Here we go", 2,"Again"]


    def test_initial_value2(self):
        obj_2 = network_collection.NetworkCollection(ipv4_network="109.156.104.31",
        raw_entry_list = [3,"Here we go", 4,"Again"])
        assert obj_2.ipv4_network == "109.156.104.31"
        assert obj_2.raw_entry_list == [3,"Here we go", 4,"Again"]



if __name__ == '__main__':
    unittest.main()
