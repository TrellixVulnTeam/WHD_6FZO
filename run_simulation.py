import time
from random import randint
from pylsl import StreamInfo, StreamOutlet
from datetime import datetime
import time
import os
import threading

data_dir=os.path.join("data")
name= "JESUS ALAN HERNANDEZ GALVAN"
info = StreamInfo('MY_ALFA_SMART', 'DATA', 5, 100, "string","myuidw43536")
outlet = StreamOutlet(info)

def sleep():
    print("Simulating data....")
    print("enviando data")
    x=0
    try:
        os.remove(os.path.join(data_dir,"sleep.txt"))
    except:
        pass
    xy=0

    while True:
        
        datax=f"{datetime.now()},{randint(40,100)},{randint(8,18)},0,{name}\n"

        with open( os.path.join(data_dir,"sleep.txt"),"a") as f:
            f.write(datax)
            x=x+1
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
                        return 1

def awake():
    x=0
    xy=0
    try:
        os.remove(os.path.join(data_dir,"array.txt"))
    except:
        pass
    while True:
        datax=f"{datetime.now()},{randint(60,100)},{randint(12,20)},{randint(95,100)},{name}\n"
        with open( os.path.join(data_dir,"array.txt"),"a") as f:
            f.write(datax)
            x+=1
        if x==336:
            with open( os.path.join(data_dir,"array.txt"),"r") as f:
                totalf=f.readlines()

            for i in totalf:
                i=i.split(",")
                for ix in range(0, len(i)): 
                    i[-1] = i[-1].strip()
                    print(i)
                    outlet.push_sample(i)
                    time.sleep(1)
                    xy=xy+1
                    if xy==224:
                        return 1
   

t1 = threading.Thread(target=sleep)
t2 = threading.Thread(target=awake)
t1.start() 
t2.start()
t1.join()  
t2.join() 


print("Done!")