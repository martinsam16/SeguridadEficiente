import dlib
import cv2, matplotlib.pyplot as plt

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("Predictors/shape_predictor_68_face_landmarks.dat")

clahe = cv2.createCLAHE(clipLimit = 1.0, tileGridSize = (6, 6))

def Iniciar(imagen):
    clahe_image = clahe.apply(imagen)
    detections = detector(clahe_image, 1)
    for k, d in enumerate(detections):
        shape = predictor(clahe_image, d)
        for i in range(1, 68):
            plt.scatter(shape.part(i).y, shape.part(i).x)
    plt.show()