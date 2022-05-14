import subprocess

####################### Requir


#Setting up network 
net = "docker network create --opt com.docker.network.bridge.name=br_test --subnet=192.168.2.0/24 NET " 
subprocess.run(net,shell=True)
print("#"*77)

#install Wiresharke
net = "sudo apt install wireshark" 
subprocess.run(net,shell=True)
print("#"*77)

#install gnome-terminal
net = "sudo apt-get install gnome-terminal" 
subprocess.run(net,shell=True)
print("#"*77)



######################### Docker file 

#docker_file for tcpdump
cmd2= "docker build -t tcpdump ./Docker_file/Tcpdump "
subprocess.run(cmd2 ,shell=True) 
print("#"*77)


#docker_file for scan
cmd2= "docker build -t nmap_scan ./Docker_file/Scan "
subprocess.run(cmd2 ,shell=True) 
print("#"*77)


#docker_file for DHCPspoofing
cmd3= "docker build -t yersinia ./Docker_file/DHCPspoofing "
subprocess.run(cmd3 ,shell=True)
print("#"*77)


#docker_file for DNSspoofing
cmd4= "docker build -t ettercap ./Docker_file/DNSspoofing "
subprocess.run(cmd4 ,shell=True)
print("#"*77)


#docker_file for ARPspoofing
cmd5= "docker build -t arp_kali ./Docker_file/ARP_kali "
subprocess.run(cmd5 ,shell=True)
print("#"*77)


#docker_file for MACflooder
cmd1= "docker pull strm/metasploit:latest "
subprocess.run(cmd1 ,shell=True)
print("#"*77)


#docker_file for IPspoofing
cmd1= "docker pul utkudarilmaz/hping3:latest "
subprocess.run(cmd1 ,shell=True)
print("#"*77)


#docker_file for Sniffing
cmd6= "docker build -t nmap_sniffing ./Docker_file/Sniffing "
subprocess.run(cmd6 ,shell=True)
print("#"*77)


#docker_file for MITMs
cmd1= "docker build -t mitm_ubuntu ./Docker_file/MITM_ubuntu "
subprocess.run(cmd1 ,shell=True)
print("#"*77)


#docker_file for MITMs
cmd1= "docker build -t mitm_kali ./Docker_file/MITM_Net_Kali "
subprocess.run(cmd1 ,shell=True)
print("#"*77)


#docker_file for Reverse
cmd1= "docker pul sauravbrahma/metasploit_image:latest "
subprocess.run(cmd1 ,shell=True)
print("#"*77)


#docker_file for SessionHijacking
cmd1= "docker build -t session_ubuntu_1 ./Docker_file/Hijack_ubuntu_1 "
subprocess.run(cmd1 ,shell=True)
print("#"*77)


#docker_file for SessionHijacking
cmd1= "docker build -t session_ubuntu_2 ./Docker_file/Hijack_ubuntu_2 "
subprocess.run(cmd1 ,shell=True)
print("#"*77)


#docker_file for SessionHijacking
cmd1= "docker pul tleemcjr/metasploitable2 "
subprocess.run(cmd1 ,shell=True)
print("#"*77)


#docker_file for SessionReset
cmd1= "docker build -t session_hping ./Docker_file/Reset_Hping_kali "
subprocess.run(cmd1 ,shell=True)
print("#"*77)


#docker_file for SessionReset
cmd1= "docker build -t session_ubuntu ./Docker_file/Reset_ubuntu_ssh "
subprocess.run(cmd1 ,shell=True)
print("#"*77)


#docker_file for dos
cmd1= "docker build -t dos_land ./Docker_file/DOS_land "
subprocess.run(cmd1 ,shell=True)
print("#"*77)


#docker_file for dos
cmd1= "docker build -t dos_random ./Docker_file/DOS_random "
subprocess.run(cmd1 ,shell=True)
print("#"*77)


#docker_file for dos
cmd1= "docker build -t dos_smurf ./Docker_file/DOS_smurf "
subprocess.run(cmd1 ,shell=True)
print("#"*77)


#docker_file for dos
cmd1= "docker build -t dos_syn ./Docker_file/DOS_SYN "
subprocess.run(cmd1 ,shell=True)
print("#"*77)


#docker_file for dos
cmd1= "docker build -t dos_sequence ./Docker_file/DOS_SEQ "
subprocess.run(cmd1 ,shell=True)
print("#"*77)

################## End Docker file 