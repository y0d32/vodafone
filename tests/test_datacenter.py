
import unittest
import sys, os

#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from  data_structures import datacenter


class TestDataCenter(unittest.TestCase):

    def testInsufficientArgs(self):
        name=""
        cluster_dict = {}

        #self.failUnlessRaises(ValueError, cluster.Cluster, name, security_level, network_dict)
        self.assertRaises(ValueError,datacenter.Datacenter, name, cluster_dict)

    def test_initial_value(self):
        obj_1 = datacenter.Datacenter(name = "I am", cluster_dict = {1:"Here we go", 2:"Again"})
        assert obj_1.name == "I am"
        assert obj_1.cluster_dict == {1:"Here we go", 2:"Again"}


    def test_initial_value2(self):
        obj_2 = datacenter.Datacenter(name = "Here we go", cluster_dict = {3:"Here we go", 4:"Again"})
        assert obj_2.name == "Here we go"
        assert obj_2.cluster_dict == {3:"Here we go", 4:"Again"}



if __name__ == '__main__':
    unittest.main()
