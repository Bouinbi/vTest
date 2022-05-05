import subprocess
from colorama import Fore
from pyfiglet import Figlet


def Install_All() : 
        

        net = "docker network create --subnet=192.168.2.0/24 NET "
        subprocess.run(net,shell=True)

        #Image of ... 
        cd1 = "pwd"
        subprocess.run(cd1,shell=True)


        #Image of ... 
        #cd1 = "docker build -t fffffff /home/joms/finaltest/LAB/LAB/Docker_file/Scan "
        #subprocess.run(cd1,shell=True)

        #subprocess.run("gnome-terminal -- bash -c 'docker build -t fffffff Docker_file/Scan ' ")


def scan() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it debien_test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 10.10.10.22 -it nmap bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)


def DHCPspoofing() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it Debien_Test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 10.10.10.22 -it yersinia bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)


def DNSspoofing() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it Debien_Test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 10.10.10.22 -it ettercap bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)


def ARPspoofing() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it ARP_kali bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 10.10.10.22 -it strm/metasploit:latest bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)


def MACflooder() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it Debien_Test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 10.10.10.22 -it strm/metasploit:latest bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)


def IPspoofing() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it Debien_Test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 10.10.10.22 -it utkudarilmaz/hping3:latest bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)



def Sniffing() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it Debien_Test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 10.10.10.22 -it --privileged ettercap bash" '
        
        #Attacker
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker2--" --name Attacker2 --network=NET --ip 10.10.10.23 -it nmap_Sniffing -sn 10.10.10.0/8 bash" '
        
        #Sniffing 
        cmd4=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)



def MITMs() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it --privileged MITM_ubuntu bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 10.10.10.22 -it --privileged  MITM_kali bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '
        
        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)


def ICMPredirection() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it --privileged MITM_ubuntu bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 10.10.10.22 -it --privileged  MITM_kali bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)

################################################# Apps Layer ############################################## 


def ReverseShell() : 

        #Run container
        subprocess.run("gnome-terminal -- bash -c  'docker run --rm -h '--Attacker--' --name Attacker --network=NET --ip 10.10.10.22 -d -it sauravbrahma/metasploit_image:latest '  ", shell=True)



        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it Debien_Test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c "docker exec -it Attacker bash" '
        cmd3=' gnome-terminal -- bash -c "docker exec -it Attacker bash" '

        #Sniffing 
        cmd4=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)
        subprocess.Popen(cmd4 ,shell=True)




def SessionHijacking() : 


        #Run container
        subprocess.run("gnome-terminal -- bash -c  'docker run --rm -h '--Attacker--' --name Attacker --network=NET --ip 10.10.10.22 -d -it Session_ubuntu_1 ' ", shell=True)
  
        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it Session_ubuntu_2 bash" '
        
        #server---metasploitable2
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Metasploitable--" --name metasploitable --network=NET --ip 10.10.10.33 -it tleemcjr/metasploitable2 bash" '
        
        #Attacker
        cmd3 = ' gnome-terminal -- bash -c " docker exec -it Attacker bash " '
        cmd4 = ' gnome-terminal -- bash -c " docker exec -it Attacker bash " '

        #Sniffing 
        cmd5=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)
        subprocess.Popen(cmd4 ,shell=True)
        subprocess.Popen(cmd5 ,shell=True)



def SessionReset() : 

        #Run container
        subprocess.run("gnome-terminal -- bash -c  'docker run --rm -h '--Attacker--' --name Attacker --network=NET --ip 10.10.10.22 -d -it Session_Hping3 ' ", shell=True)
  
        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it Session_ubuntu bash" '
        
        #Attacker
        cmd2 = ' gnome-terminal -- bash -c " docker exec -it Attacker bash " '
        cmd3 = ' gnome-terminal -- bash -c " docker exec -it Attacker bash " '

        #Sniffing 
        cmd4=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)
        subprocess.Popen(cmd4 ,shell=True)


def DOSland() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it Debien_Test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 10.10.10.22 -it DOS_land bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)



def DOSrandomSRC() : 


        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it Debien_Test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 10.10.10.22 -it DOS_random bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)




def DOS_smurf() : 


        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it Debien_Test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 10.10.10.22 -it DOS_smurf bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)


def DOS_SYN() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it Debien_Test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 10.10.10.22 -it DOS_SYN bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)


def DOS_Sequence() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 10.10.10.11 -it Debien_Test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 10.10.10.22 -it DOS_Sequence bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i docker0 -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)




