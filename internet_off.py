import subprocess 
from winotify import Notification
import multiprocessing
toast = Notification(app_id="Study Timer",
                     title="Study Time!!",
                     msg="Internet Connection Disabled",
                     icon="C:/Users/dell/Documents/GitHub/auto internet on off/study.png")

if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=subprocess.run, args=(['netsh', 'interface', 'set', 'interface', "wi-fi", "DISABLED"],))
    p2 = multiprocessing.Process(target=toast.show(), args=())
  
    # starting process 1
    p1.start()
    # starting process 2
    p2.start()
  
    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()
