# This script detects stop signs based on haar cascade on a direct video file. Also, tries to find the distance of the stop sign
import time
import cv2 as cv
import os
import glob


# Loading Haar Cascade in this case
#path1 = './Desktop/eon/online_stop.xml'
path1 ='./online_stop.xml' #that is what you use for relative path and when you do not know the platform architecture
haar_face_cascade = cv.CascadeClassifier(path1)

#path2 = max(glob.glob(os.path.join("/data/media/0/realdata/", '*/')), key=os.path.getmtime)
#path2 = '/home/oj/Desktop/eon/stopv1.hevc'
path2='./stopv1.hevc'
print(path2)

cap = cv.VideoCapture(path2)
# frame Display
while (cap.isOpened()):
    #start = time.time()
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    contours, hierarchy = cv.findContours(gray, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    stops = haar_face_cascade.detectMultiScale(gray, scaleFactor=1.22, minNeighbors=5)
    # go over list of stop signs and draw them as rectangles on original colored image
    for (x, y, w, h) in stops:
      cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
      #print("x",x,"w",w,"y",y, "h", h)
      #print ("h (pixels):", h) #h=w=~135 pixels
      #print ('Calibration - h [pixels]/12[ft]:',round(h/12.0,2)) #where h pixels at 12ft. 12 ft was known from video "12ft"
      #print "1/(h/11.0)", 1/(h/11.0) #h/12 gives~11, so divide h/11 but since more pixels means less distance so using 1/(h/11)
      dis= round(133/(h/11.3),1)  #1/(h/11) gives roughly 0.08 so 12/(1/(h/11)) gives a factor of ~140. Using it for scaling
      print 'distance(ft):',dis

    #cv.imshow('BW',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
print("existing")
cap.release()
cv.destroyAllWindows()

