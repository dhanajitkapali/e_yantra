img = cv2.imread("../Images/cat.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lower_white = np.array([0, 0, 220])
upper_white = np.array([0, 0, 255])  # for white

mask = cv2.inRange(hsv, lower_white, upper_white)
res = cv2.bitwise_and(img, img, mask=mask)

path = '../Generated/'
cv2.imwrite(os.path.join(path, 'cat_red.jpg'), res)
cv2.destroyAllWindows()
