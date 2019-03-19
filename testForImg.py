def testimg(gray):
    import matplotlib.pyplot as plt
    import cv2
    contours, hier = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])
    for ctr in contours:
        x, y, w, h = cv2.boundingRect(ctr)
        roi = gray[y:y+h, x:x+w]
        fig = plt.figure()
        d = 0
        for i in range(1, 20):
            fig.add_subplot(i, 2, 1)
            plt.imshow('character: %d'%d,roi)
            d += 1
        plt.show()