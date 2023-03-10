from flask import Flask,render_template
import time
app=Flask(__name__)
import time
# from timer import countdown,secs
# import threading
# t1 = threading.Thread(target=countdown)
# t1.start()
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/admin')
def new():
    return render_template('admin.html')


if __name__== "__main__":
    app.run(debug=True)
