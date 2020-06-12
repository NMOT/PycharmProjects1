import glob
import os
import re
ficheiroRecente  = ""
ficheiros = []
os.chdir("C:\\nkmix\\ForExcel")
for file in glob.glob("*.*"):
    #data = (file[24:41])
    alnumstring = (re.sub('[^A-Za-z0-9]+', '', data))
    #ficheiros.append(alnumstring)
    #print(file)
    ficheiros.append(file)
print(max(ficheiros))
print(ficheiros)


