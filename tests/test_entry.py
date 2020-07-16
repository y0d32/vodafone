
import unittest
import sys, os

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from  data_structures import entry


class TestEntry(unittest.TestCase):

    def testInsufficientArgs(self):
        address=""

        available=""
        last_used=""
        #self.failUnlessRaises(ValueError, cluster.Cluster, name, security_level, network_dict)
        self.assertRaises(ValueError, entry.Entry, address, available, last_used)

    def test_initial_value(self):
        obj_1 = entry.Entry(address="109.100.100.1", available="Oui", last_used="Dunno")
        assert obj_1.address == "109.100.100.1"
        assert obj_1.available == "Oui"
        assert obj_1.last_used == "Dunno"

    def test_initial_value2(self):
        obj_2 = entry.Entry(address="109.100.100.10", available="I do", last_used="N/A")
        assert obj_2.address == "109.100.100.10"
        assert obj_2.available == "I do"
        assert obj_2.last_used == "N/A"


if __name__ == '__main__':
    unittest.main()
