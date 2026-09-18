import cv2

channel = 1

def init_cap():
    url = "rtsp://admin:Qwerty%40123@192.168.1.100:554/channel" + str(channel)
    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        exit()
    return cap



cap = init_cap()

while True:

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1280, 720))
    cv2.imshow("RTSP Camera", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    if key == ord("c"):
        channel = 2 if channel == 1 else 1
        cap.release()
        cap = init_cap()


cap.release()
cv2.destroyAllWindows()