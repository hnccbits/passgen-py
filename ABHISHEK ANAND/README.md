# THIS IS A PASSWORD GENERATOR PROJECT 

## CONTENT

 - CLI TOOL 
 - LIBRARY 

# CLI tool

## This tool is used generate random password and copy that password clipboard 

[![MasterHead](https://raw.githubusercontent.com/royabhi00/passgen-py/main/ABHISHEK%20ANAND/CLI-tool/cli.png)](https://username.github.io)

## REQUIRED MODULES

```python
import pyperclip
```

```python
import argparse
```

## TOOLS

- `-pl` :- this will take password lenght  
- `-w` :- this will take website name
- `-lw` :- this take number of lower case alphabet
- `-up` :- this take number of upper case alphabet
- `-d` :- this will number of digit
- `-s` :- this will take number of special character

## NOTE

- MINIMUM PASSWORD LENGTH SHOULD BE 15
- SUM OF THE NUMBERS OF DIFFRENT CHARACTERS SHOULD BE LESS THAN OR EQUAL TO THE PASSWORD LENGTH YOU ENTERED

## DEFAULT VALUES OF THE FLAGS

If the user uses the without using of any flags `-pl` `-w` `-lw` `-up` `-d` `-s` , then it will generate a password of 15 Characters with 4 lowercase, 3 uppercase, 5 numerals, and 3 special characters and default website as Facebook 


## How to use the tool

- get the `indexpy.py` (Location `passgen-py/ABHISHEK ANAND/CLI-tool)
- install `pyinstaller` using command 
```python
pip3 install pyinstaller 
```
- make exe file of `indexpy.py` using command 
```python 
pyinstaller indexpy.py
```
- get the `indexpy.py` exe file `passgen-py/ABHISHEK ANAND/CLI-tool/dist/indexpy`
- run `indexpy` using above given tools

# LIBRARY

## This Library is useful to create Passwords, copy them in clipboard

[![MasterHead](https://raw.githubusercontent.com/royabhi00/passgen-py/main/ABHISHEK%20ANAND/library/lib.png)](https://username.github.io)

## About the Library

This is a library for the random password generation.

## Locating the module
```python
cd passgen-py/ABHISHEK ANAND/library/passgenerator/dist
```


## Installing the module

```python
pip3 install PASSGENERATOR-0.0.1-py3-none-any.whl
```

## Importing the module
```python
import passgenpackage
```

## How to use the module

import the module as desribed above.
use it as a function by 
```python
passgenpackage.passgenerator(w, pl, lw, up, d, s)
```

 # 
 
| Arguments            |       Description                                                                                  |
| ---------------------|----------------------------------------------------------------------------------------------------| 
|`- w`   | is used for giving website name|
|`-pl`   | is used to give length of the password you want|
|`- lw`  | is for number of lowercase chaaracters.|
|`- up`  | is for number of uppercase chaaracters.|
|`- n`   |is for number of numerals.|
|`- s`   |is for number of special chaaracters|

#
