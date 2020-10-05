from pylsl import StreamInlet, resolve_stream, resolve_bypred
from engine import daily
from threading import Thread
print("Buscando datos en red....")

streams = resolve_stream('name', 'MY_ALFA_SMART')

inlet = StreamInlet(streams[0])
x=0
xy=0
data=[]

while True:
    sample, timestamp = inlet.pull_sample()
    print(sample,timestamp)
    x=x+1
    print(x)
    data.append(sample)
    if x == 100:
        exit(0)
    else:
        t= Thread(target=daily(data))
        t.start()
        t.join()
