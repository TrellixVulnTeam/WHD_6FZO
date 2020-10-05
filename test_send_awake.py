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
print("enviando data")

def main():
    x=0
    name= "JESUS ALAN HERNANDEZ GALVAN"
    try:
        os.remove(os.path.join(data_dir,"array.txt"))
    except:
        pass
    xy=0
    while True:
        
        datax=f"{datetime.now()},{randint(60,100)},{randint(12,20)},{randint(95,100)},{name}\n"

        with open( os.path.join(data_dir,"array.txt"),"a") as f:
            f.write(datax)
            x+=1
        if x==500:
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