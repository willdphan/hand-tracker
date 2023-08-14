import cv2
import mediapipe as mp
import time

# grab default cam
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
# can edit params, but we can just use default
hands = mpHands.Hands()
# formality required
mpDraw = mp.solutions.drawing_utils

# initialize previous time
pTime = 0
# initialize current time
cTime = 0

# infinite loop
while True:
    # returns if successful and image/video captured
    success, img = cap.read()
    # convert to RGB b/c hands class only uses RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # call hands object and use .process to process imgRGB frame
    results = hands.process(imgRGB)
    # below checks whether something is printed or not
    # print(results.multi_hand_landmarks)

    # if something in frame...
    if results.multi_hand_landmarks:
        # for each hand landmark in results.multi_hand_landmarks
        for handLms in results.multi_hand_landmarks:
            # id number and landmark coordination find inside handLms.landmark
            for id, lm in enumerate(handLms.landmark):
                # get height, width, and channels of img
                h, w, c = img.shape
                # find position. convert normalized lm coords to pixel coords
                # landmark x val * width, landmark y val * height
                # gives us cx and cy positions (pixel coords of image)
                cx, cy = int(lm.x * w), int(lm.y * h)
                # need to print id or else we won't know which is which
                print(id, cx, cy)
                # draws circles on certain index or all index
                # if id == 4:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            # use mpDraw to display original image and hand landmark
            # hand_connections provide green hand lines
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    # gives current time
    cTime = time.time()
    # frames per second
    fps = 1 / (cTime - pTime)
    # previous time becomes current time
    pTime = cTime

    # display frames per second with this. Use integers, gives positions, 
    # font, scale, color, and thickness
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    # show image/video
    cv2.imshow("Image", img)
    # wait 1 ms
    cv2.waitKey(1)