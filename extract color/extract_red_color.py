img = cv2.imread("../Images/cat.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#method one
lower_red = np.array([0, 100, 0])
upper_red = np.array([5, 255, 255])

#method two
## Range for lower range
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

## Range for upper range
lower_red = np.array([170, 120, 70])
upper_red = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red, upper_red)

mask = mask1 + mask2

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img, img, mask=mask)

path = '../Generated/'
cv2.imwrite(os.path.join(path, 'cat_red.jpg'), res)
cv2.destroyAllWindows()
