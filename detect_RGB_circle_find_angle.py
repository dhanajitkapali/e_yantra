angle = 0.00
img = ip_image  #read the image
h = int(img.shape[0] / 2)
w = int(img.shape[1] / 2)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 100, 0])
upper_red = np.array([5, 255, 255])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img, img, mask=mask)

gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

gray_blurred = cv2.blur(gray, (3, 3))

detected_circles = cv2.HoughCircles(gray_blurred,
                                    cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                                    param2=30, minRadius=1, maxRadius=40)

if detected_circles is not None:

    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        cv2.circle(res, (a, b), r, (0, 255, 0), 2)

        cv2.circle(res, (a, b), 1, (0, 0, 255), 3)

lower_green = np.array([36, 25, 25])
upper_green = np.array([70, 255, 255])  # for green

mask = cv2.inRange(hsv, lower_green, upper_green)
gres = cv2.bitwise_and(img, img, mask=mask)

gray = cv2.cvtColor(gres, cv2.COLOR_BGR2GRAY)

gray_blurred = cv2.blur(gray, (3, 3))

detected_circles = cv2.HoughCircles(gray_blurred,
                                    cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                                    param2=30, minRadius=1, maxRadius=40)

if detected_circles is not None:

    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        c, d, s = pt[0], pt[1], pt[2]

        cv2.circle(gres, (c, d), s, (0, 255, 0), 2)

        cv2.circle(gres, (c, d), 1, (0, 0, 255), 3)


def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))

    return ang + 360 if ang < 0 else ang


# print(getAngle((h, w), (a, b), (c, d)))
# print(getAngle((a, b), (c, d), (h, w)))
# print(getAngle((a, b), (h, w), (c, d)))
# print(getAngle((c, d), (a, b), (h, w)))
# print(getAngle((h, w), (c, d), (a, b)))
angle = getAngle((c, d), (h, w), (a, b))

## Your Code goes here
###########################
cv2.imshow("window", ip_image)
cv2.waitKey(0);
return angle