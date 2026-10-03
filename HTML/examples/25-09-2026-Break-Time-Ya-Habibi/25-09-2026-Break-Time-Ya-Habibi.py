import webbrowser
import time
start_time = time.ctime() 
print("Start Time:", start_time)
start = 1
target = 10
while start <= target:
    webbrowser.open("https://www.youtube.com/watch?v=M6_rH8jfAvw")
    time.sleep(2*60*60)
    start = start +1