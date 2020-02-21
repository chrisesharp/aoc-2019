import unittest
from netdriver import NetDriver
from nic import NIC, Network

class NetTest(unittest.TestCase):
    def test_nic(self):
        nic = NIC(0)
        nw = Network()
        nic.connect(nw)
        nic.append(1)
        nic.append(2)
        nic.append(3)
        nic.append(4)
        self.assertEqual(0,nic.pop())
        self.assertEqual(1,nic.pop())
        self.assertEqual(2,nic.pop())
        self.assertEqual(3,nic.pop())
        self.assertEqual(4,nic.pop())
        self.assertEqual(-1,nic.pop())
        self.assertEqual(-1,nic.pop())
    
    def test_nic_2(self):
        nic_zero = NIC(0)
        nic_one = NIC(1)
        nw = Network()
        nic_zero.connect(nw)
        nic_one.connect(nw)
        nic_zero.append(1)
        nic_zero.append(2)
        nic_one.append(3)
        nic_one.append(4)
        self.assertEqual(0,nic_zero.pop())
        self.assertEqual(1,nic_one.pop())
        self.assertEqual(2,nic_zero.pop())
        self.assertEqual(3,nic.pop())
        self.assertEqual(4,nic.pop())
        self.assertEqual(-1,nic.pop())
        self.assertEqual(-1,nic.pop())

    # def test_net_program(self):
    #     net = NetDriver("input.txt")
    #     network = Network()
    #     net.connect(1, network)
    #     output = net.read_msg()
    #     expected = ()
    #     self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()


