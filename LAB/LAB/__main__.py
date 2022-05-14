#!/usr/bin/python3
import click
import datetime
import pyfiglet
from pyfiglet import Figlet
import time
import progressbar
from colorama import Fore,init
from pathlib import Path


from LAB.Function import scan,DHCPspoofing,DNSspoofing,ARPspoofing,MACflooder,IPspoofing,Sniffing,MITMs,ICMPredirection,ReverseShell,SessionHijacking,SessionReset,DOSland,DOSrandomSRC,DOS_smurf,DOS_SYN,DOS_Sequence


# Print name of Tools using pyfiglet 
print(Fore.GREEN  + '\n')
f = Figlet(font='standard')
init(autoreset=True)
print(f.renderText("   Witchattacks "))

print('    v2.2')
init(autoreset=True)
print(Fore.BLUE + '    https://github.com/Ensaodocker ')
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


# For Option : using click library 
@click.command()
@click.option("--name", prompt=Fore.GREEN  + """[+] Please enter attack number : 
                 \n\t1  - scan \n\t2  - DNSspoofing \n\t3  - DHCPspoofing \n\t4  - ARPspoofing \n\t5  - MACflooder \n\t6  - IPspoofing \n\t7  - Sniffing \n\t8  - MITMs \n\t9  - ICMPredirection \n\t10 - ReverseShell \n\t11 - SessionHijacking \n\t12 - SessionReset \n\t13 - DOSland \n\t14 - DOSrandomSRC \n\t15 - DOS_smurf \n\t16 - DOS_SYN \n\t17 - DOS_Sequence \n\n --> Attack  """


, help="""Provide your attacks name : 
          \n\t1  - scan /\n\t2 - DNSspoofing /\n\t3  - DHCPspoofing /\n\t4  - ARPspoofing /\n\t5  - MACflooder /\n\t6  - IPspoofing 
          \n\t7  - Sniffing /\n\t8  - MITMs /\n\t9  - ICMPredirection /\n\t10 - ReverseShell /\n\t11 -  SessionHijacking /\n\t12 -  SessionReset 
          \n\t13 - DOSland /\n\t14 -  DOSrandomSRC /\n\t15 -  DOS_smurf /\n\t16 -  DOS_SYN /\n\t17 -  DOS_Sequence """)



#main function
def main(name):
    print('')
    time.sleep(0.4)


    if name == '1' :
        scan()

    elif name == '2' :
        DNSspoofing()

    elif name == '3' :
        DHCPspoofing()

    elif name == '4' :
        ARPspoofing()

    elif name == '5' :
        MACflooder()

    elif name == '6' :
        IPspoofing()

    elif name == '7' :
        Sniffing()

    elif name == '8' :
        MITMs()

    elif name == '9' :
        ICMPredirection()

    elif name == '10' :
        ReverseShell()

    elif name == '11' :
        SessionHijacking()

    elif name == '12' :
        SessionReset()

    elif name == '13' :
        DOSland()

    elif name == '14' :
        DOSrandomSRC()

    elif name == '15' :
        DOS_smurf()

    elif name == '16' :
        DOS_SYN()

    elif name == '17' :
        DOS_Sequence()                   

    else : 
        print('\nPlease enter a Correct number attack , Show help for more details ( --help )')



