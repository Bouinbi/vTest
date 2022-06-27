# vTest

vTest is a Linux tool for testing different network attacks, we used Docker and Python to build it 

## Modules Installation 

Use the package manager [pip](https://pip.pypa.io/en/stable/) and requirements.txt file to install python modules.

```bash
pip install -r requirements.txt 
```

## Installation

Before the instalation of witchattack tool, you must install dockerfile images, so run this python script  ' Install_Docker_file.py ' in main folder :

- Go to vTest Folder and run 

```bash
sudo Python3 Install_Docker_file.py
```

now, you can Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Wtichattack .

- Go to vTest Folder and run ( . is in the command )

```bash
sudo pip3 install -e .
```

## Usage

```bash
vTest --name <ATTACK_NAME>
```

OR Just type vTest and will get a list of available attacks :

```bash
vTest 
```

For more info :
```bash
vTest --help
```
## Uninstall 

```bash
sudo pip3 uninstall vTest
```
