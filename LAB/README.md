# InfoGet

Witchattack is a Linux tool for testing different network attacks, we used Docker and Python to build it 
## Modules Installation  


Use the package manager [pip](https://pip.pypa.io/en/stable/) and requirements.txt file to install python modules.

```bash
pip install -r requirements.txt 
```

## Installation

Before the instalation of witchattack tools, you must install dockerfile images, so run the script python ' Install_Docker_file.py ' in main folder 

- Go to LAB Folder and run 

```bash
sudo Python3 Install_Docker_file.py
```

now yuo can Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Wtichattack .

- Go to LAB Folder and run ( . is in the command )

```bash
sudo pip3 install -e .
```

## Usage

```bash
LAB --name <ATTACK_NAME>
```


OR Just type LAB and will get a list of available attacks :

```bash
LAB 
```

For more info :
```bash
LAB --help
```
## Uninstall 

```bash
sudo pip3 uninstall LAB
```
