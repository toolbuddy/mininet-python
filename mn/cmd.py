"""
    Creating simple cli mininet with python
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
# log/error
from mininet.log import output, error

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
	    switch = self.addSwitch('s1')
            # Python's range(N) generates 0..N-1
            for h in range(n):
                host=self.addHost('h%s' % (h+1))
                self.addLink(host,switch)

def start_CLI():
    topo = SingleSwitchTopo(n=6)
    net = Mininet(topo)
    net.start()
    # enter into mininet CLI
    CLI(net)
    # "exit" the cli
    print "Close the CLI"
    net.stop()

# create 
def mycmd(self,line):
    "mycmd is an example command to extend the Mininet CLI"
    net = self.mn
    output( 'mycmd invoked for', net, 'with line', line, '\n'  )
CLI.do_mycmd = mycmd

if __name__ == '__main__':
    # start cli
    start_CLI()