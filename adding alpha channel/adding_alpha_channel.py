image = cv2.imread("../Images/flowers.jpg")

for alpha in np.arange(0, 0.6, 0.5)[::-1]:
    overlay = image.copy()
    output = image.copy()
    cv2.rectangle(overlay, (0, image.shape[1] + 1500), (image.shape[0] + 1500, 0), (255, 255, 255), -1)
    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)

    # cv2.imwrite('flowers_alpha.png', output)
    path = '../Generated/'
    cv2.imwrite(os.path.join(path, 'flowers_alpha.png'), output)
    break

cv2.destroyAllWindows()