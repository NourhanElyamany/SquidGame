import cv2

# read camera
# use motion detection if camera is seeing shit,
# else do nothing

def brightImage(grayFrame):
    blur = cv2.blur(gray, (5, 5))
    mean = cv2.mean(blur)[0]
    return mean > 90

video = cv2.VideoCapture(0)

while True:
    _, frame1 = video.read()
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    cv2.imshow('trial', frame1)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()   
cv2.destroyAllWindows()