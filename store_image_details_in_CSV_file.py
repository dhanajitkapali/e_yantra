#imgs is storing file name of images
imgs = ['bird', 'cat', 'flowers', 'horse']
h = []
w = []
c = []
for i in range(0, len(imgs)):
    img = cv2.imread("../Images/" + imgs[i] + ".jpg")
    h = img.shape[0]
    w = img.shape[1]
    c = img.shape[2]
    m = int(h / 2)
    n = int(w / 2)
    px_intensity = []
    for j in range(0, 3):
        px_intensity.append(img[m, n, j])

    df = pd.DataFrame(
        {"name": imgs[i] + ".jpg", "height": [h], "width": [w], "channel": [c], "intensity_blue": px_intensity[0],
         "intensity_green": px_intensity[1], "intensity_red": px_intensity[2]})
    if not os.path.exists("../Generated/stats.csv"):
        df.to_csv("../Generated/stats.csv", index=False)
    else:
        df.to_csv("../Generated/stats.csv", mode='a', index=False, header=False)
