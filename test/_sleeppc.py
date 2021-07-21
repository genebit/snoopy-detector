import os
import time

for i in range(1, 6):
    time.sleep(1)
    print(i)
    
    if i == 4:
        print('!Show image!')

    elif i == 5:
        print('Sleep')
        # os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")