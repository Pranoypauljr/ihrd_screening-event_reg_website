from flask import Flask,render_template
import time
app=Flask(__name__)
def countdown():
    flag=0
    while(flag==0):
        days=1
        hrs=23
        mins=59
        secs=59
        timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days,hrs,mins, secs)
        time.sleep(1)
        t-=1
        if(secs==0&mins==0&hrs==0&days==0):
            flag=1
            continue
        elif(secs==0&mins==0&hrs==0):
            secs=59
            mins=59
            hrs=59
            days-=1
            time.sleep(1)
        elif(secs==0&mins==0):
            secs=59
            mins=59
            hrs-=1
            time.sleep(1)
        elif(secs==0):
            secs=59
            mins-=1
            time.sleep(1)
        else:
            secs-=1
            time.sleep(1)
        print(timer, end="\r")

            


@app.route('/')
def index():

    return render_template('index.html')
@app.route('/admin')
def new():
    return render_template('admin.html')


if __name__== "__main__":
    app.run(debug=True)
