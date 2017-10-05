import cv2,time, numpy as np, os, pyautogui

pyautogui.FAILSAFE = False

def Image_processing():
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        # If able to read image then moving ahead
        if ret:
            hight, width, c = frame.shape
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # For filtering of signal
            lower_red = np.array([30,140,80])
            upper_red = np.array([255,255,180])
            mask = cv2.inRange(hsv , lower_red , upper_red)
            res = cv2.bitwise_and(frame, frame, mask = mask)

            # For getting the largest area
            hierarchy, contours, _ = cv2.findContours(mask, 1, 2)
            area = 0
            temp = 0
            flag = 0
            i = 0
            j = 0
            for cnt in contours:
                area_t = cv2.contourArea(cnt)
                area = area + area_t
                if (temp < area_t):
                    flag = 1
                    temp = area_t
                    j = i
                i = i + 1

            # for getting largest dead part centroid
            if (flag != 0):
                c = contours[j]
                M = cv2.moments(c)

                x,y,w,h = cv2.boundingRect(c)
                aspect_ratio = float(w)/h

                if (int(M['m00'] != 0)):
                    cX = int(M['m10']/M['m00'])
                    cY = int(M['m01']/M['m00'])

                    # normalaise with display
                    disY = cY*900/hight-80
                    disX = 1450 - cX*1600/width
                    if disX < 1:
                        disX = 1
                    if disX > 1365:
                        disX = 1365
                    if disY < 1:
                        disY = 1
                    if disY > 760:
                        disY = 760

                    print 'position is ' , disX, ' --- ', disY

                    print 'aspect ratio -- ', aspect_ratio

                    if aspect_ratio < .3:
                        pyautogui.click()
                    elif aspect_ratio > 3:
                        num = -10
                        if disY > 500:
                            num = 10
                        pyautogui.scroll(num)
                    else:
                        pyautogui.moveTo(disX, disY)

                cv2.drawContours(res, [c], -1, (0, 255, 255), 1)

                # Showing Different parts
                cv2.namedWindow('frame1',cv2.WINDOW_NORMAL)
                cv2.imshow('frame1',res)
                k = cv2.waitKey(5) & 0xFF
                if k == 27:
                    break

            else:
                print 'can\'t see the signal'
                time.sleep(1)
                cap.release()
                cap = cv2.VideoCapture(0)

        else:
            print "Can't read frame"
            break

    cv2.destroyAllWindows()
    cap.release()

