img = cv2.imread("../Images/cat.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lower_green = np.array([36, 25, 25])
upper_green = np.array([70, 255, 255])  # for green

mask = cv2.inRange(hsv, lower_green, upper_green)
res = cv2.bitwise_and(img, img, mask=mask)

path = '../Generated/'
cv2.imwrite(os.path.join(path, 'cat_red.jpg'), res)
cv2.destroyAllWindows()
