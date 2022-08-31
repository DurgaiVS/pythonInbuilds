from distutils.log import error
import errno
from msilib.schema import Error
import re
from xml.dom.pulldom import ErrorHandler

txt = 'There is heavy rain in the spain'
x = re.search("^T\w+", txt)
print(x.span())
print(x.string)
print(x.group())
z = re.findall("\s", txt)
print(z if z else 'Siiiiuuu')
y = re.sub(r"\s", "_", txt, 2)
print(y if y else 'No')
w = re.split('\s', txt, 3)
print(w if w else 'Nuu') 
try:
    x = 10
    print(x + 'HII')
    f = open("./test.py", 'w')
    try:
        f.write("Yea buddy, Light Weight")
    finally:
        f.close()
except :
    print('Error Occured')
    raise ErrorHandler("No, No, No, No")
else:
    print('Executed successfully')
finally:
    print("Completed annyhow")