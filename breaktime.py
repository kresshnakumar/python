import time
import webbrowser

no_of_breaks = 3;
count = 1;
print("started at:"+time.ctime());
while (count <= no_of_breaks):
    print("break  at:"+time.ctime());
    time.sleep(10);
    webbrowser.open("https://www.youtube.com/watch?v=5KL-JAe4KfM");
    count= count + 1;
