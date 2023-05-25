import subprocess 
from winotify import Notification
import multiprocessing
toast = Notification(app_id="Study Timer",
                     title="Enjoy!!",
                     msg="Internet Connection Enabled",
                     icon="C:/Users/dell/Documents/GitHub/auto internet on off/study.png")

if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=subprocess.run, args=(['netsh', 'interface', 'set', 'interface', "wi-fi", "ENABLED"],))
    p2 = multiprocessing.Process(target=toast.show())
  
    # starting process 1
    p1.start()
    # starting process 2
    p2.start()
  
    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()