import os
import shutil
import time
os.mkdir('CS')
file = open('homework.txt','w')
with open('homework.txt','w') as file:
    file.write('4112029028_林志勳')
shutil.copy('homework.txt','CS')
items = os.listdir('CS')
for item in items:
    with open(os.path.join("CS",item),'r') as innerfile:
        text = innerfile.read()
        print(text)
    size = os.path.getsize(item)
    print(f"File size:{size}")
    mtime = os.path.getmtime(item)
    ftime = time.ctime(mtime)
    print(f"Last edit time:{ftime}")
if os.path.exists('homework.txt'):
    os.remove('homework.txt')
shutil.rmtree('CS')