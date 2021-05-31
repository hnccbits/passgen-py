# This CLI tool is used to generate passwords and copy it to the clipboard

[](https://github.com/royabhi00/passgen-py/blob/main/CLI-tool/cli.png)

## REQUIRED MODULES

```python
import pyperclip
```

```python
import argparse
```

## TOOLS

`-pl` :- this will take password lenght  
`-w` :- this will take website name
`-lw` :- this take number of lower case alphabet
`-up` :- this take number of upper case alphabet
`-d` :- this will number of digit
`-s` :- this will take number of special character

## NOTE

- MINIMUM PASSWORD LENGTH SHOULD BE 15
- SUM OF THE NUMBERS OF DIFFRENT CHARACTERS SHOULD BE LESS THAN OR EQUAL TO THE PASSWORD LENGTH YOU ENTERED

## DEFAULT VALUES OF THE FLAGS

If the user uses the without using of any flags `-pl` `-w` `-lw` `-up` `-d` `-s` , then it will generate a password of 15 Characters with 4 lowercase, 3 uppercase, 5 numerals, and 3 special characters and default website as Facebook 



