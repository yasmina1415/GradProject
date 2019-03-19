#.........................................segmentation..........................................................#
def segmentation(gray):
    import cv2
    import matplotlib.pyplot as plt
    import numpy as np
    cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU,gray)
    contours, hier = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])
    cv2.imshow("contours", gray)
    cv2.waitKey(0)
    d=0
    for ctr in contours:
        # Get bounding box
        x, y, w, h = cv2.boundingRect(ctr)
        # Getting ROI
        roi = gray[y:y+h, x:x+w]
        #->
        cv2.imshow('character: %d'%d,roi)
        #cv2.imwrite('character_%d.png'%d, roi)
        d+=1
