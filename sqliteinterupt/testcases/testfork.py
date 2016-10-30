"forks child processes until you type 'q'"
import os
import time
def child():
    for i in range(0,50):
        time.sleep(1)
        print('Hello from child', os.getpid())

    #print os.execl("python","-al")
    os._exit(0) # else goes back to parent loop

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            for i in range(0, 50):
                time.sleep(1.2)
                #print('Hello from child', os.getpid())
                print('Hello from parent', os.getpid(), newpid)
        if input() == 'q': break

parent()