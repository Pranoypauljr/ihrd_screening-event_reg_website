import time
def countdown():
    flag=0
    days=1
    hrs=23
    mins=59
    secs=10
    while(flag==0):
        timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days,hrs,mins, secs)
        time.sleep(1)
        if(secs==0 and mins==0 and hrs==0 and days==0):
            flag=1
            continue
        elif(secs==0 and mins==0 and hrs==0):
            secs=59
            mins=59
            hrs=59
            days-=1
        elif(secs==0 and mins==0):
            secs=59
            mins=59
            hrs-=1
        elif(secs==0):
            secs=59
            mins-=1
        else:
            secs-=1
        print(timer, end="\r")
countdown()