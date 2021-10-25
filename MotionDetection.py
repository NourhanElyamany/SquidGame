import cv2

video = cv2.VideoCapture('vtest.avi')

fr, frame1 = video.read()
fr, frame2 = video.read()

firstFrame = None

while video.isOpened():

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0) #blurring the frame
    _, thresholdFrame = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) # to select the first variable
    thresholdFrame = cv2.dilate(thresholdFrame, None, iterations = 2) # apply layer of smoothining -- iteration is for how accurate the smoothing will be, if increased then the program will capture the noise also
   
    # contours is for the motion of any obj in the frame :

    cntr,hierarchy = cv2.findContours(thresholdFrame.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   
    # to avoid considering small noise as contour , specify contour vector :

    for contour in cntr:

        if cv2.contourArea(contour) < 1000 : # hygiene
            continue

        (x,y,w,h) = cv2.boundingRect(contour)   # draw a bounding rectangle around the moved obj
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        # cv2.drawContours(frame1, cntr, -1, (0, 255, 0), 2) 

    cv2.imshow('trial', frame1)
    frame1 = frame2
    fr, frame2 = video.read()
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()   
cv2.destroyAllWindows()