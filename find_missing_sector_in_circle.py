## Your Code goes here
## placeholder image
sector_image = np.ones(ip_image.shape[:2], np.uint8) * 255
## check value is white or not
print(sector_image[0, 0])
## Your Code goes here

img = ip_image     #read the image from images folder

x = int(img.shape[0] / 2)
y = int(img.shape[1] / 2)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_white = np.array([0, 0, 0])
upper_white = np.array([0, 0, 255])  # for white

mask = cv2.inRange(hsv, lower_white, upper_white)
res = cv2.bitwise_and(img, img, mask=mask)

res1 = res

for i in range(x - 20, x + 20):
    for j in range(y - 20, y + 20):
        res1[i, j, :] = 0

a, b, i = 0, 0, 0
for i in range(1, 512):
    f = 0
    for a in range(1, i):
        b = (i * i) - (a * a)
        b = int(math.sqrt(b))
        if res1[x + a, y + b, 0] > 200 and res1[x + a, y + b, 1] > 200 and res1[x + a, y + b, 2] > 200 and res1[
            x - a, y + b, 0] > 200 and res1[x - a, y + b, 1] > 200 and res1[x - a, y + b, 2] > 200 and res1[
            x + a, y - b, 0] > 200 and res1[x + a, y - b, 1] > 200 and res1[x + a, y - b, 2] > 200 and res1[
            x - a, y - b, 0] > 200 and res1[x - a, y - b, 1] > 200 and res1[x - a, y - b, 2] > 200:
            f = 1
        else:
            f = 2
    if f == 1:
        break

min = 30
max = 50
for s in range(0, 1024):
    for r in range(0, 1024):
        if (x - s) * (x - s) + (y - r) * (y - r) > (i - min) * (i - min) and (x - s) * (x - s) + (y - r) * (y - r) < (
                i + max) * (i + max):
            res1[s, r, :] = 0

result = 255 - res1
sector_image = result

###########################
cv2.imshow("window", sector_image)
cv2.waitKey(0);
return sector_image
