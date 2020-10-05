import time
from random import randint
from pylsl import StreamInfo, StreamOutlet
from datetime import datetime
import time
import os

info = StreamInfo('MY_ALFA_SMART', 'DATA', 5, 100, "string","myuidw43536")
outlet = StreamOutlet(info)
data_dir=os.path.join("data")
print("Simulating data....")

fc=[60,100]
fr=[12,20]
so=[95,100]

print("enviando data")
total=[]
x=0
name= "JESUS ALAN HERNANDEZ GALVAN"

try:
    os.remove(os.path.join(data_dir,"sleep.txt"))
except:
    pass
xy=0
while True:
    
    datax=f"{datetime.now()},{randint(40,100)},{randint(8,18)},0,{name}\n"

    with open( os.path.join(data_dir,"sleep.txt"),"a") as f:
        f.write(datax)
        x+=1
    if x==190:
        with open( os.path.join(data_dir,"sleep.txt"),"r") as f:
            totalf=f.readlines()

        for i in totalf:
            i=i.split(",")
            for ix in range(0, len(i)): 
                i[-1] = i[-1].strip()
                print(i)
            outlet.push_sample(i)
            time.sleep(1)
            xy=xy+1
            if xy==120:
                exit(0)