from flask import Flask, render_template, Response
import cv2, sys, numpy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    i=1
    while i<10:
        yield (b'--frame\r\n'
            b'Content-Type: text/plain\r\n\r\n'+str(i)+b'\r\n')
        i+=1

def get_frame():
    ramp_frames=100
    capturar=cv2.VideoCapture(0) #Se pondría la ip del cliente y con la del server procesamos y ponemos en red
    rostro=[]
    i=1
    ClasificadorRostro = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_alt.xml')
    while True:
        booleano, frame = capturar.read()
        rostro = numpy.array(ClasificadorRostro.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5))
        for (x, y, w, h) in rostro:
            cv2.rectangle(frame, (x, y), (x + w,  y + h), (500, 600, 10), 1)

        imgencode=cv2.imencode('.jpg',frame)[1]
        stringData=imgencode.tostring()
        yield (b'--frame\r\n'
            b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')
        i+=1
    del(capturar)

@app.route('/calc')
def calc():
     return Response(get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='192.168.0.102', debug=True, threaded=True)
