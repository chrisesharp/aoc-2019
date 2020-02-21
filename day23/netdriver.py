from opcodes import Processor, get_program
from nic import NIC, Network

class NetDriver():
    def __init__(self, input):
        self.program = get_program(input)
        self.proc = Processor(self.program, 1024)
        self.nic = None
    
    def connect(self, addr, network):
        self.nic = NIC(addr)
        self.nic.connect(network)
        self.proc.set_std_input(self.nic)
        return self
    
    def tick(self):
        written = 0
        while not self.nic.cpu_read:
            self.proc.step()
        self.nic.cpu_read = False
        while len(self.proc.stdout) >= 3:
            dest = self.proc.stdout.pop(0)
            packet = self.proc.stdout[:2]
            self.proc.stdout = self.proc.stdout[2:]
            self.nic.send(dest, packet)
            written = 1
        return written

def run_network(network, computers):
    part_1_completed = False
    zero_y = []
    while True:
        written = 0
        for i in range(100):
            written += computers[i%50].tick()
            if not part_1_completed and network.nat_has_packet():
                print ("Part 1:", network.NAT[0][1])
                part_1_completed = True
        if not written and network.nat_has_packet():
            packet = network.NAT.pop()
            network.write(0, packet)
            zero_y.append(packet[1])
            if len(zero_y) > 1 and zero_y[-1]==zero_y[-2]:
                print("Part 2:",packet[1])
                break



if __name__ == '__main__':
    network = Network()
    computers = []
    
    for i in range(50):
        computers.append(NetDriver("input.txt").connect(i, network))
    print("Computers booted and attached to network")
    run_network(network, computers)
