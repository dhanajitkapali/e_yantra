img = cv2.imread("../Images/horse.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
B, G, R = cv2.split(img)
I = ((0.3 * R) + (0.59 * G) + (0.11 * B))
# I=np.add(0.3*R,0.59*G,0.11*B)
zeros = np.zeros(img.shape[:2], dtype="uint8")
path = '../Generated/'
cv2.imwrite(os.path.join(path, 'horse_gray.jpg'), gray_img)

