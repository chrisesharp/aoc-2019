class Network():
    def __init__(self):
        self.queues = {}
        self.NAT = []
    
    def connect(self, addr):
        self.queues[addr] = []
    
    def write(self, dest, packet):
        if dest == 255:
            self.NAT = [packet]
        else:
            self.queues[dest].append(packet)

    def read(self, addr):
        if queue := self.queues.get(addr):
            return queue.pop(0)
        return []

    def nat_has_packet(self):
        return self.NAT

class NIC():
    def __init__(self, addr):
        self.addr = addr
        self.net = None
        self.buffer = [addr]
        self.cpu_read = False

    def connect(self, net):
        self.net = net
        net.connect(self.addr)
    
    def send(self, dest, packet):
        self.net.write(dest,packet)
    
    def receive(self):
        packet = None
        for packet in self.net.read(self.addr):
            self.buffer.append(packet)
        return packet
 
    def pop(self):
        self.cpu_read = True
        if self.buffer or self.receive():
            return self.buffer.pop(0)
        return -1
        