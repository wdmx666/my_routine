from skimage import transform
from skimage import io
import path
import itertools

fp = path.Path('resources')
sp = path.Path(".protocol_images")

ct = itertools.count()
for item in fp.files():
    img = io.imread(item)
    new_img = transform.rescale(img, 800/img.shape[1])
    io.imsave(sp.joinpath(item.basename()), new_img)
    print(ct.__next__())




# print(img.shape)  #图片原始大小
# print(transform.rescale(img, 0.1).shape)  #缩小为原来图片大小的0.1倍
# print(transform.rescale(img, [0.5,0.25]).shape)  #缩小为原来图片行数一半，列数四分之一
# print(transform.rescale(img, 2).shape)   #放大为原来图片大小的2倍