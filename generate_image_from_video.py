cam = cv2.VideoCapture("../Videos/RoseBloom.mp4")

currentframe = 0

while (True):

    ret, frame = cam.read()

    if ret:

        name = '../Generated/' + 'frame_as_6.jpg'
        print('Creating...' + name)

        if currentframe == 150:
            cv2.imwrite(name, frame)
            break
        currentframe += 1
    else:
        break