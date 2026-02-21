import platform
import argparse
import subprocess
import ipaddress
from concurrent.futures import ThreadPoolExecutor

class Scanner:
    def __init__(self):
        # this is the main command so i dont need to copy paste it when checking the os
        self.command = ["ping","1"] 
        self.os = platform.system().lower() # We get the os windows/linux/mac

        # Handles the os command because windows and linux are diffrent
        if self.os == "windows": # if windows we inser the flag -n
            self.command.insert(1,"-n")

        else: # if linux/mac we insert flasg -c
            self.command.insert(1,"-c")

    def get_atribute(self,atrb:str,result):
        for line in result.stdout.splitlines():
            if atrb.lower() in line.lower():
                for part in line.split():
                    if part.lower().startswith(atrb + "="):
                        part = part.split("=")
                        return int(part[1])




    def ping_host(self,host_obj):
        host_ip = str(host_obj)
        current_cmd = self.command + [str(host_ip)]
        time,ttl = None,None
        #  This is the main command for pinging devices subprocess.run
        try:
            result = subprocess.run(  #The basic structure you'll be using:
                current_cmd, # The command (as a list)
                capture_output=True,       # Tells Python to "listen" to the output
                text=True,         # Tells Python to treat the output as a string, not bytes
                timeout = 2                  
            )
            time = self.get_atribute("time",result)
            ttl = self.get_atribute("ttl",result)


            if result.returncode == 0:
                return host_ip,True,ttl,time
            else:
                return host_ip,False,ttl,time
        except:
            return host_ip,False,ttl,time
    
    def scan_network(self,network_prefix:str,workers):
        try:
            # ipadress.ip_network() converts our network_prefix into a obkect that has all hosts
            network = ipaddress.ip_network(network_prefix) 
            with ThreadPoolExecutor(workers) as exe:
                results = exe.map(self.ping_host,network.hosts())
                
            for host_ip,host_is_up,ttl,time in results:
                if host_is_up:
                    print(f"[+] Host at ip {str(host_ip)} is up.")
                    if ttl != None:
                        if ttl >= 120:
                            print(f"Host is probaly a windows device ttl={ttl}.")
                        elif ttl >= 60:
                            print(f"Host is probably a linux device ttl={ttl}")
                        print(f"Host took {time} to respond")
            

        except ValueError:
            print(f"The network prefix {network_prefix} is not valid.")



def main():
    parser = argparse.ArgumentParser(description="A tool for scaning if hosts are up")
    parser.add_argument("-n","--network",help="The network prefix (ex: 192.168.1.0/24)",required=True)
    parser.add_argument("-w","--workers",help="Number of threads to run on the higer the faster",default=30,type=int)
    args = parser.parse_args()

    scan = Scanner()
    scan.scan_network(args.network,args.workers)

main()