
import unittest
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from  data_structures import cluster



class TestCluster(unittest.TestCase):

    def testInsufficientArgs(self):
        name=""
        network_dict = {}
        security_level=""
        #self.failUnlessRaises(ValueError, cluster.Cluster, name, security_level, network_dict)
        self.assertRaises(ValueError,cluster.Cluster, name, security_level, networks)

    def test_initial_value(self):
        obj_1 = cluster.Cluster(name = "I am", network_dict = {1:"Here we go", 2:"Again"}, security_level=23)
        assert obj_1.name == "I am"
        assert obj_1.networks == {1:"Here we go", 2:"Again"}
        assert obj_1.security_level == 23

    def test_initial_value2(self):
        obj_2 = cluster.Cluster(name = "Here we go", networks = {3:"Here we go", 4:"Again"}, security_level=24)
        assert obj_2.name == "Here we go"
        assert obj_2.networks == {3:"Here we go", 4:"Again"}
        assert obj_2.security_level == 24


if __name__ == '__main__':
    unittest.main()
