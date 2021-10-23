import cv2 , time

video = cv2.VideoCapture(0)

firstFrame = None

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0) #blurring the frame

    # fixing the first frame as a reference frame

    if firstFrame is None :
        firstFrame = gray
        continue
    deltaFrame =  cv2.absdiff(firstFrame,gray)  # to find the difference between frames

    thresholdFrame = cv2.threshold(deltaFrame,50,255,cv2.THRESH_BINARY)[0] # to select the first variable

    thresholdFrame = cv2.dilate(thresholdFrame, None, iterations = 2) # apply layer of smoothining -- iteration is for how accurate the smoothing will be, if increased then the program will capture the noise also
    

    # contours is for the motion of any obj in the frame :

    (cntr,_) = cv2.findContours(thresholdFrame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # to avoid considering small noise as contour , specify contour vector :

    for contour in cntr:
        if cv2.contourArea(contour) < 1000 :
            continue
        (x,y,w,h) = cv2.boundingRect(contour)   # draw a bounding rectangle around the moved obj

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow('trial', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()   
cv2.destroyAllWindows()