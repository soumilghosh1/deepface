import cv2
from deepface import DeepFace
img = cv2.imread("crying.jpg")
results = DeepFace.analyze(img)
print(results)
