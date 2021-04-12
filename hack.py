import sys
import os
arr=sys.argv.copy()
arr.pop(0)  #0-id,1-start,2-step,3-endin
step=int(arr[2])*500
arr[1]=int(arr[1])
arr[3]=int(arr[3])
if step>0 :
    theRange= range(arr[1],arr[3],step)
else:
    theRange=range(arr[3],arr[1],step)


for i in theRange:
    print(f'{arr[0]} {i} {arr[2]}    {i+step}')
    os.popen(f"start python latestp.py {arr[0]} {i} {arr[2]} {i+step}")
