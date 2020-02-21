import unittest
from netdriver import NetDriver
from nic import NIC, Network

class NetTest(unittest.TestCase):
    def test_nic(self):
        nw = Network()
        nic = NIC(0)
        nic.connect(nw)
        nic.send(0,[1,2])
        nic.send(0,[3,4])
        self.assertEqual(0,nic.pop())
        self.assertEqual(1,nic.pop())
        self.assertEqual(2,nic.pop())
        self.assertEqual(3,nic.pop())
        self.assertEqual(4,nic.pop())
        self.assertEqual(-1,nic.pop())
        self.assertEqual(-1,nic.pop())
    
    def test_nic_2(self):
        nw = Network()
        nic_zero = NIC(0)
        nic_one = NIC(1)
        nic_zero.connect(nw)
        nic_one.connect(nw)
        nic_zero.send(1,[2,3])
        nic_one.send(0,[4,5])
        self.assertEqual(1,nic_one.pop())
        self.assertEqual(2,nic_one.pop())
        self.assertEqual(3,nic_one.pop())
        self.assertEqual(0,nic_zero.pop())
        self.assertEqual(4,nic_zero.pop())
        self.assertEqual(5,nic_zero.pop())
        self.assertEqual(-1,nic_one.pop())
        self.assertEqual(-1,nic_zero.pop())

    def test_net_program(self):
        network = Network()
        nd = NetDriver("input.txt").connect(10, network)
        self.assertEqual(10, nd.nic.pop())
        self.assertEqual([], network.queues[10])

if __name__ == '__main__':
    unittest.main()


