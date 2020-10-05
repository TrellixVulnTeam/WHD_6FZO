import test_send_awake
import test_send_sleep
import threading

def main():
    t1 = threading.Thread(target=test_send_awake.main)
    t2 = threading.Thread(target=test_send_sleep.main)
    t1.start() 
    t2.start() 
    t1.join() 
    t2.join() 

    print("Done!")
main()