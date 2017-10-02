#This is the code for my HW5
import re

readfile = open('actualdata.txt', 'r')
content = readfile.readlines()

x = list() 

for line in content:
    y = re.findall('[0-9]+',line)
    x = x + y
sum=0
for numb in x:
    sum = sum + int(numb)

print (sum)