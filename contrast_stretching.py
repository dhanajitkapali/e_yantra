
img = #read the image from images folder
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]

max_b = b.max()
max_g = g.max()
max_r = r.max()

min_b = b.min()
min_g = g.min()
min_r = r.min()

mb = 255 / (max_b - min_b)
mg = 255 / (max_g - min_g)
mr = 255 / (max_r - min_r)

cb = 255 - mb * max_b
cg = 255 - mg * max_g
cr = 255 - mr * max_r

img[:, :, 0] = mb * img[:, :, 0] + cb
img[:, :, 1] = mg * img[:, :, 1] + cg
img[:, :, 2] = mr * img[:, :, 2] + cr
return img
