#!/usr/bin/python3
import click
import datetime
import pyfiglet
from pyfiglet import Figlet
import time
import progressbar
from colorama import Fore,init

from LAB.Function import Install_All,scan,DHCPspoofing,DNSspoofing,ARPspoofing,MACflooder,IPspoofing,Sniffing,MITMs,ICMPredirection,ReverseShell,SessionHijacking,SessionReset,DOSland,DOSrandomSRC,DOS_smurf,DOS_SYN,DOS_Sequence


# Print name of Tools using pyfiglet 
print(Fore.GREEN  + '\n')
f = Figlet(font='standard')
init(autoreset=True)
print(f.renderText("   Witchattacks "))

print('    v2.2')
init(autoreset=True)
print(Fore.BLUE + '    https://github.com/Bouinbi')
print('   ',Fore.GREEN  + str(datetime.datetime.now()))
print('\n')




# Print Progress Bar :
def animated_marker(x):
    widgets = [Fore.GREEN + 'Loading :  ', progressbar.AnimatedMarker()]
    init(autoreset=True)
    bar = progressbar.ProgressBar(widgets=widgets).start()
    for i in range(x):
        time.sleep(0.1)
        bar.update(i)       
# Driver's code
animated_marker(10)
print('\n')


# For Option  using click library 
@click.command()
@click.option("--name", prompt=Fore.GREEN  + """[+] Please enter attack name : 
                 \n\t+ Install_All \n\t+ scan \n\t+ DHCPspoofing \n\t+ ARPspoofing \n\t+ MACflooder \n\t+ IPspoofing
                 \n\t+ Sniffing \n\t+ MITMs \n\t+ ICMPredirection \n\t+ ReverseShell \n\t+ SessionHijacking \n\t+ SessionReset    
                 \n\t+ DOSland \n\t+ DOSrandomSRC \n\t+ DOS_smurf \n\t+ DOS_SYN \n\t+ DOS_Sequence                                        
                 \n\n --> Attack  """


, help="""Provide your attacks name : 
          Install_All,scan / DHCPspoofing / DNSspoofing / ARPspoofing / MACflooder / IPspoofing 
          Sniffing / MITMs / ICMPredirection / ReverseShell / SessionHijacking / SessionReset 
          DOSland / DOSrandomSRC / DOS_smurf / DOS_SYN / DOS_Sequence """)



#main function
def main(name):
    print('')
    animated_marker(5)

    #Install all docker file and create network 

    if name == 'install' :
        Install_All()

    if name == 'scan' :
        scan()

    if name == 'install' :
        Install_All()

    if name == 'DHCPspoofing' :
        DHCPspoofing()

    if name == 'ARPspoofing' :
        ARPspoofing()

    if name == 'MACflooder' :
        MACflooder()

    if name == 'IPspoofing' :
        IPspoofing()

    if name == 'Sniffing' :
        Sniffing()

    if name == 'MITMs' :
        MITMs()

    if name == 'ICMPredirection' :
        ICMPredirection()

    if name == 'ReverseShell' :
        ReverseShell()

    if name == 'SessionHijacking' :
        SessionHijacking()

    if name == 'SessionReset' :
        SessionReset()

    if name == 'DOSland' :
        DOSland()

    if name == 'DOSrandomSRC' :
        DOSrandomSRC()

    if name == 'DOS_SYN' :
        DOS_SYN()

    if name == 'DOS_Sequence' :
        DOS_Sequence()
                                       
        

    else : 
        print('\nPlease enter the Correct attack name, Show help for more details ( --help )')
