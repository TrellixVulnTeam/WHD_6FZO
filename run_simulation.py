import test_send_awake
import test_send_sleep
import threading
import test_recive

def main():
    t1 = threading.Thread(target=test_send_awake)
    t2 = threading.Thread(target=test_send_sleep)
    t1.start() 
    t2.start() 
    t1.join() 
    t2.join() 

    print("Done!") 