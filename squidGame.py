import cv2

# while True:
#     # read camera
#     # use motion detection if camera is seeing shit,
#     # else do nothing
#     pass


blur = cv2.blur(image, (5, 5))  # With kernel size depending upon image size
if cv2.mean(blur) > 127:  # The range for a pixel's value in grayscale is (0-255), 127 lies midway
    print('light') # (127 - 255) denotes light image
else:
    print('dark') # (0 - 127) denotes dark image