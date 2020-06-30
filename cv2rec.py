import cv2
#from cv2 import VideoCapture, CascadeClassifier, waitKey
y = 0
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(<enter file path.mp4>)
print('hi')
pedestrian_cascade = cv2.CascadeClassifier(r'<use own path>')
while True:
    # reads frames from a video
    ret, frames = cap.read()
    # convert to gray scale of each frames
    #gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    # Detects pedestrians of different sizes in the input image
    pedestrians = pedestrian_cascade.detectMultiScale( frames, 1.1, 
    1)
    # To draw a rectangle in each pedestrians
    for (x,y,w,h) in pedestrians:
       y = y+1
    # Wait for Enter key to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   
